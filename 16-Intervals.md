# 16 · Intervals

> **Prereqs:** 09, 15 · **Time:** 2 days

## When to use

- The input is a list of `[start, end]` pairs: meetings, bookings, ranges.
- Merging, inserting, counting overlaps, or finding the minimum number of rooms or arrows.

## Core concepts

- Two intervals overlap if `a.start <= b.end and b.start <= a.end`. Check whether the boundaries are inclusive.
- **Sort by start** for merging and inserting.
- **Sort by end** for "the most non-overlapping intervals" or "the fewest arrows". This is the classic activity-selection greedy.
- **Minimum number of rooms**: use a min-heap of end times, or a **sweep line** (+1 at each start, −1 at each end, sorted).
- Intersecting two sorted lists: use two pointers and advance whichever interval ends first.

## Templates

```python
# Merge
intervals.sort()
res = [intervals[0]]
for s, e in intervals[1:]:
    if s <= res[-1][1]:
        res[-1][1] = max(res[-1][1], e)
    else:
        res.append([s, e])

# Max non-overlapping (activity selection)
intervals.sort(key=lambda x: x[1])
count, end = 0, float('-inf')
for s, e in intervals:
    if s >= end:
        count += 1; end = e

# Meeting rooms II: heap of end times
intervals.sort()
h = []
for s, e in intervals:
    if h and h[0] <= s: heapq.heappop(h)
    heapq.heappush(h, e)
return len(h)
```

## Pitfalls

- Whether touching intervals like `[1,2]` and `[2,3]` count as overlapping depends on the problem. Read it carefully.
- Sorting by start when the greedy approach needs sorting by end.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 252 | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) 🔒 | E | Sort + check neighbours |
| [ ] | 56 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | M | Sort by start ⭐ |
| [ ] | 57 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | M | Three phases |
| [ ] | 435 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | M | Sort by end |
| [ ] | 452 | [Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) | M | Sort by end |
| [ ] | 986 | [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/) | M | Two pointers |
| [ ] | 253 | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) 🔒 | M | Heap / sweep line ⭐ |
| [ ] | 1851 | [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | H | Sort queries + heap |

## My Notes

-
