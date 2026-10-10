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

```java
// Merge
Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
List<int[]> res = new ArrayList<>();
for (int[] cur : intervals) {
    int[] last = res.isEmpty() ? null : res.get(res.size() - 1);
    if (last != null && cur[0] <= last[1]) last[1] = Math.max(last[1], cur[1]);
    else res.add(cur);
}
return res.toArray(new int[0][]);

// Max non-overlapping (activity selection)
Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1]));
int count = 0;
long end = Long.MIN_VALUE;
for (int[] iv : intervals)
    if (iv[0] >= end) {
        count++;
        end = iv[1];
    }

// Meeting rooms II: heap of end times
Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
PriorityQueue<Integer> h = new PriorityQueue<>();
for (int[] iv : intervals) {
    if (!h.isEmpty() && h.peek() <= iv[0]) h.poll();
    h.offer(iv[1]);
}
return h.size();
```

## Pitfalls

- Whether touching intervals like `[1,2]` and `[2,3]` count as overlapping depends on the problem. Read it carefully.
- Sorting by start when the greedy approach needs sorting by end.
- Sorting with `(a, b) -> a[0] - b[0]`. It overflows when values span the full `int` range (Minimum Number of Arrows has exactly this test). Use `Integer.compare`.

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
