# 05 · Binary Search

> **Prereqs:** 00 · **Time:** 3–4 days

## When to use

- A sorted array, or one that is sorted but rotated.
- O(log n) is required, or n is around 10⁹.
- **Binary search on the answer**: "find the minimum speed, capacity or time such that the task is feasible", where feasibility is **monotonic** (once it becomes true, it stays true).
- Finding a boundary: the first or last occurrence, or a lower or upper bound.

## Core concepts

- Think of binary search as finding **the first index where `cond(i)` is True** in a sequence like `F F F T T T`.
- Calculate `mid = (lo + hi) // 2`. In Go, C++ or Java, use `lo + (hi - lo) / 2` to avoid overflow.
- Rotated array: one half is always sorted, so work out which half it is and whether the target falls inside it.
- Python's `bisect_left` returns the first index with `a[i] >= x`, and `bisect_right` returns the first index with `a[i] > x`.

## Templates

```python
# Universal: first index where cond is True (lo..hi inclusive search space)
def first_true(lo, hi, cond):
    while lo < hi:
        mid = (lo + hi) // 2
        if cond(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo   # check cond(lo) if "no answer" is possible

# Binary search on answer (e.g. Koko)
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if hours_needed(mid) <= h: hi = mid
    else: lo = mid + 1
return lo

# Classic exact match
l, r = 0, len(a) - 1
while l <= r:
    m = (l + r) // 2
    if a[m] == t: return m
    if a[m] < t: l = m + 1
    else: r = m - 1
return -1
```

## Pitfalls

- Infinite loops from mixing up the templates (`lo < hi` with `hi = mid`, versus `lo <= hi` with `hi = mid - 1`). Pick one template and stick to it.
- Setting the wrong search bounds for binary search on the answer (lo and hi must include every possible answer).
- Rotated arrays with duplicates, which make the worst case O(n).

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 704 | [Binary Search](https://leetcode.com/problems/binary-search/) | E | Classic |
| [ ] | 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | E | Lower bound |
| [ ] | 74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | M | Flatten the index |
| [ ] | 34 | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | M | Two boundaries |
| [ ] | 875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | M | Search on the answer |
| [ ] | 1011 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | M | Search on the answer |
| [ ] | 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | M | Compare with the right end |
| [ ] | 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | M | Find the sorted half |
| [ ] | 162 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | M | Follow the slope |
| [ ] | 981 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | M | bisect on timestamps |
| [ ] | 410 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | H | Search on the answer |
| [ ] | 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | H | Partition search |

## My Notes

-
