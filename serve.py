#!/usr/bin/env python3
"""Serve the DSA prep site locally, with a chat panel backed by Claude Code.

    python3 serve.py            # then open http://localhost:8765

Each chat message runs `claude -p` in this folder, so Claude can answer
questions and edit the topic .md files. Whenever a .md file changes, the
site is rebuilt and the page reloads.
"""
import json
import subprocess
import sys
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT = 8765

SYSTEM_PROMPT = """\
You are the chat assistant embedded in the user's DSA (data structures & algorithms) prep website.
Your working directory holds the site's source:
- README.md: roadmap, pacing plan, interview checklist, revision log
- NN-<Topic>.md: one file per topic with concepts, Python templates, pitfalls, a LeetCode problem table and a "My Notes" section
- images/: SVG figures referenced from the notes
The site is rebuilt automatically after you edit any .md file. Never run the build yourself.

Your role is DSA tutor and study planner:
- Answer concept questions clearly and concisely in markdown, with small Python examples when useful.
- When the user is stuck on a problem, give progressive hints. Only give a full solution when they ask for one.
- When they ask to change the plan, notes, problem lists or pacing, or to add an explanation, edit the relevant .md files directly. Keep the existing structure, and keep problem rows in exactly this format so the site can parse them:
  | [ ] | <number> | [<Title>](https://leetcode.com/problems/<slug>/) | E/M/H | <Pattern> |
  Only add real LeetCode problems with correct numbers and URLs.
- Only touch files inside this folder. After editing, say in one line what you changed.
Each user message starts with a [Context] block showing which page they are on and their progress. Use it, but don't repeat it back."""

ALLOWED_TOOLS = ["Read", "Edit", "Write", "Glob", "Grep", "WebSearch", "WebFetch"]


def md_snapshot():
    return {p.name: p.stat().st_mtime_ns for p in ROOT.glob("*.md")}


def rebuild():
    subprocess.run([sys.executable, str(ROOT / "build.py")], cwd=ROOT, check=True, capture_output=True)


def tool_detail(name, inp):
    if "file_path" in inp:
        return Path(inp["file_path"]).name
    for key in ("pattern", "query", "url"):
        if key in inp:
            return str(inp[key])[:80]
    return ""


class Handler(SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # keep the terminal quiet

    def do_GET(self):
        if self.path == "/api/health":
            return self._json({"ok": True})
        return super().do_GET()

    def do_POST(self):
        if self.path != "/api/chat":
            return self.send_error(404)
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        message = (body.get("message") or "").strip()
        if not message:
            return self.send_error(400, "empty message")
        prompt = f"[Context]\n{body.get('context', '')}\n[/Context]\n\n{message}"

        cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
               "--include-partial-messages", "--permission-mode", "acceptEdits",
               "--allowedTools", *ALLOWED_TOOLS, "--disallowedTools", "Bash",
               "--append-system-prompt", SYSTEM_PROMPT]
        if body.get("session_id"):
            cmd += ["--resume", body["session_id"]]

        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        before = md_snapshot()
        proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=subprocess.DEVNULL, text=True)
        try:
            for line in proc.stdout:
                try:
                    ev = json.loads(line)
                except json.JSONDecodeError:
                    continue
                self._relay(ev)
            proc.wait()
            if proc.returncode not in (0, None) and not getattr(self, "_got_result", False):
                self._send({"t": "error", "text": proc.stderr.read()[-800:] or f"claude exited with code {proc.returncode}"})
            if md_snapshot() != before:
                rebuild()
                self._send({"t": "rebuilt"})
            self._send({"t": "end"})
        except (BrokenPipeError, ConnectionResetError):
            proc.kill()  # browser hit Stop or closed the tab
            if md_snapshot() != before:
                rebuild()

    def _relay(self, ev):
        kind = ev.get("type")
        if kind == "stream_event":
            e = ev.get("event", {})
            if e.get("type") == "content_block_delta" and e.get("delta", {}).get("type") == "text_delta":
                self._send({"t": "delta", "text": e["delta"]["text"]})
            elif e.get("type") == "message_start":
                self._send({"t": "turn"})
        elif kind == "assistant":
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    self._send({"t": "tool", "name": block.get("name"), "detail": tool_detail(block.get("name"), block.get("input") or {})})
        elif kind == "result":
            self._got_result = True
            self._send({"t": "done", "session_id": ev.get("session_id"), "is_error": ev.get("is_error"),
                        "error": ev.get("result") if ev.get("is_error") else None})

    def _send(self, obj):
        self.wfile.write((json.dumps(obj) + "\n").encode())
        self.wfile.flush()

    def _json(self, obj):
        data = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    rebuild()
    server = ThreadingHTTPServer(("127.0.0.1", PORT), partial(Handler, directory=str(ROOT)))
    url = f"http://localhost:{PORT}/"
    print(f"DSA Prep running at {url}  (Ctrl+C to stop)")
    if "--no-open" not in sys.argv:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
