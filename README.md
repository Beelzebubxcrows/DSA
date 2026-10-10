# DSA Prep

Topic-wise prep. In each file, read the concepts and templates first, then solve the problems in order (Easy, then Medium, then Hard).
Templates are in Java, written with the standard library (`HashMap`, `ArrayDeque`, `PriorityQueue`, `TreeMap`) the way you'd write them in an interview. The Pitfalls sections include Java-specific traps such as `int` overflow, `Integer` comparison and comparator overflow.

## Revision site

**Start it with the chat panel (recommended):**

```bash
cd ~/Projects/Resume/Preparation/DSA
python3 serve.py        # opens http://localhost:8765. Press Ctrl+C to stop.
```

Click **💬 Ask Claude** (bottom right) to ask questions, get hints, or have Claude update your plan and notes. Claude can see which page you're on and your progress. It runs as Claude Code in this folder and can edit the `.md` files, but it can't run shell commands. When it changes a file, the site rebuilds and the page reloads automatically.

You can also just open `index.html` directly, without the chat. In that case, **after editing any `.md`, run `python3 build.py`** and refresh the page.

- **Dashboard:** overall progress, activity heatmap, the next problems to do.
- **Topic pages:** the notes plus a problem table. Log each attempt as ✓ (solved on my own), ~ (needed a hint) or ✗ (couldn't solve).
- **Revise:** problems that are due for a re-solve (spaced repetition), plus three flashcard decks: **Pattern drill** (problem → approach), **Spot the technique** (signal → topic) and **Template recall**.
- **Problems:** every problem in one place, filterable. **Templates:** a one-page cheat sheet of all the templates.
- **Hide patterns** blurs the pattern column so it doesn't give the answer away.

Progress is saved in your browser. Use **Export** to back it up, and **Import** to restore it. The browser treats `http://localhost:8765` and the plain `index.html` file as separate sites, so each keeps its own progress. Pick one and stick with it, or move progress across with Export and Import.

## How to use each topic file

1. **Read** the "When to use" and "Core concepts" sections.
2. **Type out the templates** from memory. Don't just read them.
3. **Solve the problems**: try each one for 25–30 minutes before looking at hints. Tick `[x]` when you can solve it on your own.
4. **Write notes** in "My Notes": what tripped you up, edge cases, and the key insight in one line.
5. **Revisit** the problems you couldn't solve after 3 days, then 7, then 21.

## Roadmap (suggested order)

Each phase depends on the ones before it. Do them in order.

| # | Topic | Phase | Status |
|---|-------|-------|--------|
| 00 | [Complexity Analysis](00-Complexity-Analysis.md) | Foundations | ⬜ |
| 01 | [Arrays & Hashing](01-Arrays-and-Hashing.md) | Foundations | ⬜ |
| 02 | [Two Pointers](02-Two-Pointers.md) | Linear | ⬜ |
| 03 | [Sliding Window](03-Sliding-Window.md) | Linear | ⬜ |
| 04 | [Stack & Monotonic Stack](04-Stack.md) | Linear | ⬜ |
| 05 | [Binary Search](05-Binary-Search.md) | Linear | ⬜ |
| 06 | [Linked List](06-Linked-List.md) | Linear | ⬜ |
| 07 | [Trees](07-Trees.md) | Non-linear | ⬜ |
| 08 | [Tries](08-Tries.md) | Non-linear | ⬜ |
| 09 | [Heaps / Priority Queue](09-Heaps.md) | Non-linear | ⬜ |
| 10 | [Backtracking](10-Backtracking.md) | Recursion | ⬜ |
| 11 | [Graphs](11-Graphs.md) | Graphs | ⬜ |
| 12 | [Advanced Graphs](12-Advanced-Graphs.md) | Graphs | ⬜ |
| 13 | [Dynamic Programming: 1D](13-DP-1D.md) | DP | ⬜ |
| 14 | [Dynamic Programming: 2D](14-DP-2D.md) | DP | ⬜ |
| 15 | [Greedy](15-Greedy.md) | Misc | ⬜ |
| 16 | [Intervals](16-Intervals.md) | Misc | ⬜ |
| 17 | [Math & Geometry](17-Math-and-Geometry.md) | Misc | ⬜ |
| 18 | [Bit Manipulation](18-Bit-Manipulation.md) | Misc | ⬜ |
| 19 | [Advanced (Optional)](19-Advanced-Optional.md) | Stretch | ⬜ |

Status key: ⬜ not started · 🟨 in progress · ✅ done · 🔁 needs revision

## Pacing (about 10 weeks at 2–3 problems a day)

| Weeks | Topics |
|-------|--------|
| 1 | 00–03 |
| 2 | 04–06 |
| 3 | 07–09 |
| 4 | 10 |
| 5 | 11–12 |
| 6–7 | 13–14 |
| 8 | 15–19 |
| 9–10 | Mixed revision, company-tagged problems, mock interviews |

## Interview loop checklist (use on every problem)

1. Restate the problem and confirm the input/output format.
2. Ask about constraints: size of n, value range, duplicates, negatives, empty input.
3. Work through a small example by hand.
4. Describe the brute-force solution and its complexity.
5. Optimise it, naming the pattern you're using.
6. Code it while talking through what you're doing.
7. Dry-run your code on the example, then on edge cases.
8. State the final time and space complexity.

## Revision log

| Date | Problem | Topic | Result (Solved / Hint / Failed) | Revisit on |
|------|---------|-------|----------------------------------|------------|
| | | | | |
