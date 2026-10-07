#!/usr/bin/env python3
"""Build index.html from the topic markdown files.

Re-run after editing any .md file:  python3 build.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

topics = []
for path in sorted(ROOT.glob("[0-9][0-9]-*.md")):
    text = path.read_text(encoding="utf-8")
    title = text.splitlines()[0].lstrip("#").strip()
    topics.append({"id": path.stem, "file": path.name, "title": title, "md": text})

data = {
    "topics": topics,
    "readme": (ROOT / "README.md").read_text(encoding="utf-8"),
}
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

template = (ROOT / "site" / "template.html").read_text(encoding="utf-8")
(ROOT / "index.html").write_text(template.replace("/*__DATA__*/null", payload), encoding="utf-8")

problems = sum(len(re.findall(r"^\| \[[ xX]\] \|", t["md"], re.M)) for t in topics)
print(f"Built index.html: {len(topics)} topics, {problems} problems")
