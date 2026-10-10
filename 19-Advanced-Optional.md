# 19 · Advanced (Optional)

> Do this topic only after 00–18 feel solid. These come up rarely in typical SDE interviews, mostly at Google or in hard rounds. Knowing they **exist** and when to mention them is usually enough.

## Topics

### Segment Tree / Fenwick Tree (BIT)
- **When:** range queries (sum, min or max) combined with **point updates**, each in O(log n).
- A Fenwick tree is shorter to write and handles prefix sums. A segment tree is more flexible and can support lazy propagation for range updates.

```java
class BIT {
    int[] t;
    BIT(int n) { t = new int[n + 1]; }
    void update(int i, int d) {      // 1-indexed
        for (; i < t.length; i += i & -i) t[i] += d;
    }
    int query(int i) {               // prefix sum [1..i]
        int s = 0;
        for (; i > 0; i -= i & -i) s += t[i];
        return s;
    }
}
```

### String matching: KMP / Rabin-Karp / Z-function
- **When:** finding a pattern inside a text in O(n + m), or finding the longest prefix that is also a suffix.
- The KMP failure function (LPS array) is the most important part to learn.

### Monotonic queue DP, bitmask DP, digit DP
- **Bitmask DP:** `dp[mask][i]` for small n (≤ 20), as in the travelling salesman problem or "visit all nodes".

### Topological sort + DP on DAGs, Strongly Connected Components (Kosaraju or Tarjan)

### Ordered sets
- In Java, `TreeSet` / `TreeMap` give O(log n) insert, delete, `floor`, `ceiling`, `lower` and `higher`. They don't support rank queries (the index of an element), so use a BIT or segment tree for those.

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
