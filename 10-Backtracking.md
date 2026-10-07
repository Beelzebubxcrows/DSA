# 10 · Backtracking

> **Prereqs:** recursion, 07 · **Time:** 4–5 days

## When to use

- "Generate **all**" subsets, permutations, combinations, partitions or valid configurations.
- Constraint satisfaction problems: N-Queens, Sudoku, searching for a word in a grid.
- n is small (≤ 20 or so), so exponential time is expected.

## Core concepts

- The pattern is **choose → explore → un-choose**.
- Think of the solution as a **decision tree**. Each level is one decision.
- **Subsets**: include or skip each element. **Combinations**: pass a `start` index so you never go backwards. **Permutations**: use a `used[]` array.
- **Handling duplicates**: sort first, then skip `nums[i] == nums[i-1]` when `i > start` (or when the previous duplicate is unused, for permutations).
- **Pruning**: stop early once a branch can't succeed (for example, the sum already exceeds the target).
- Complexity: subsets is O(n·2ⁿ) and permutations is O(n·n!).

## Templates

```python
# Subsets / combinations
res, path = [], []
def bt(start):
    res.append(path[:])              # copy!
    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i-1]: continue  # dedupe (sorted)
        path.append(nums[i])
        bt(i + 1)                    # i (not i+1) if reuse allowed
        path.pop()
bt(0)

# Permutations
used = [False] * n
def bt():
    if len(path) == n:
        res.append(path[:]); return
    for i in range(n):
        if used[i]: continue
        used[i] = True; path.append(nums[i])
        bt()
        used[i] = False; path.pop()

# Grid backtracking (word search)
def dfs(r, c, i):
    if i == len(word): return True
    if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[i]: return False
    tmp, board[r][c] = board[r][c], '#'
    found = any(dfs(r+dr, c+dc, i+1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
    board[r][c] = tmp
    return found
```

## Pitfalls

- Appending `path` instead of `path[:]`, which means every result ends up pointing to the same list.
- Forgetting to undo the choice (the pop, or restoring a grid cell).
- Getting the dedupe condition wrong, or forgetting to sort first.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 78 | [Subsets](https://leetcode.com/problems/subsets/) | M | Include/skip |
| [ ] | 90 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | M | Sort + dedupe |
| [ ] | 39 | [Combination Sum](https://leetcode.com/problems/combination-sum/) | M | Reuse allowed |
| [ ] | 40 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | M | No reuse + dedupe |
| [ ] | 46 | [Permutations](https://leetcode.com/problems/permutations/) | M | Used array |
| [ ] | 47 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | M | Used array + dedupe |
| [ ] | 17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | M | Product of choices |
| [ ] | 22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | M | Track open/close counts |
| [ ] | 79 | [Word Search](https://leetcode.com/problems/word-search/) | M | Grid backtracking |
| [ ] | 131 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | M | Partition |
| [ ] | 51 | [N-Queens](https://leetcode.com/problems/n-queens/) | H | Sets for columns and diagonals |
| [ ] | 37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | H | Constraint satisfaction |

## My Notes

-
