# 19 · Advanced (Optional)

> Do this topic only after 00–18 feel solid. These come up rarely in typical SDE interviews, mostly at Google or in hard rounds. Knowing they **exist** and when to mention them is usually enough.

## Topics

### Segment Tree / Fenwick Tree (BIT)
- **When:** range queries (sum, min or max) combined with **point updates**, each in O(log n).
- A Fenwick tree is shorter to write and handles prefix sums. A segment tree is more flexible and can support lazy propagation for range updates.

```python
class BIT:
    def __init__(self, n): self.t = [0] * (n + 1)
    def update(self, i, d):          # 1-indexed
        while i < len(self.t):
            self.t[i] += d; i += i & -i
    def query(self, i):              # prefix sum [1..i]
        s = 0
        while i > 0:
            s += self.t[i]; i -= i & -i
        return s
```

### String matching: KMP / Rabin-Karp / Z-function
- **When:** finding a pattern inside a text in O(n + m), or finding the longest prefix that is also a suffix.
- The KMP failure function (LPS array) is the most important part to learn.

### Monotonic queue DP, bitmask DP, digit DP
- **Bitmask DP:** `dp[mask][i]` for small n (≤ 20), as in the travelling salesman problem or "visit all nodes".

### Topological sort + DP on DAGs, Strongly Connected Components (Kosaraju or Tarjan)

### Ordered sets
- In Python, `sortedcontainers.SortedList` (available on LeetCode) gives O(log n) insert, delete and rank queries.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 28 | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | E | KMP |
| [ ] | 307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | M | BIT / segment tree |
| [ ] | 847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | H | BFS + bitmask |
| [ ] | 315 | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | H | BIT / merge sort |
| [ ] | 214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | H | KMP |

## My Notes

-
