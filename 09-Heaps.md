# 09 · Heaps / Priority Queue

> **Prereqs:** 01 · **Time:** 2–3 days

## When to use

- "Top K", "Kth largest or smallest", "K closest".
- Repeatedly taking the min or max as the data changes (scheduling, simulations).
- Merging K sorted lists or streams.
- **Median of a stream**: use two heaps.
- Dijkstra's algorithm and Prim's algorithm (topic 12).

## Core concepts

- A binary heap gives O(log n) push and pop and O(1) peek. `heapify` takes O(n).
- Python's `heapq` is a **min-heap** only. For a max-heap, push `-x`.
- **Top K largest**: keep a **min-heap of size K**. This takes O(n log k).
- Push tuples like `(priority, tiebreak, item)` when the items can't be compared with each other.
- **Two heaps for the median**: a max-heap holds the lower half and a min-heap holds the upper half. Keep their sizes within 1 of each other.
- **Quickselect** finds the Kth element in O(n) on average. It's a good optimisation to mention.

## Templates

```python
import heapq

# K largest with min-heap of size k
h = []
for x in nums:
    heapq.heappush(h, x)
    if len(h) > k: heapq.heappop(h)
return h[0]  # kth largest

# Max-heap via negation
h = [-x for x in nums]; heapq.heapify(h)
largest = -heapq.heappop(h)

# Merge k sorted lists
h = [(node.val, i, node) for i, node in enumerate(lists) if node]
heapq.heapify(h)
while h:
    val, i, node = heapq.heappop(h)
    ...
    if node.next: heapq.heappush(h, (node.next.val, i, node.next))

# Two heaps median
lo, hi = [], []          # lo = max-heap (negated), hi = min-heap
def add(x):
    heapq.heappush(lo, -x)
    heapq.heappush(hi, -heapq.heappop(lo))
    if len(hi) > len(lo): heapq.heappush(lo, -heapq.heappop(hi))
def median():
    return -lo[0] if len(lo) > len(hi) else (-lo[0] + hi[0]) / 2
```

## Pitfalls

- Pushing objects that can't be compared, which causes a TypeError. Add an index as a tiebreaker.
- Forgetting to negate the value back when using a max-heap.
- Using a heap when sorting once would be simpler.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 703 | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | E | Min-heap of size k |
| [ ] | 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | E | Max-heap |
| [ ] | 973 | [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | M | Heap of size k ⭐ |
| [ ] | 215 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | M | Heap / quickselect |
| [ ] | 621 | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | M | Heap + cooldown queue |
| [ ] | 767 | [Reorganize String](https://leetcode.com/problems/reorganize-string/) | M | Greedy with a max-heap |
| [ ] | 355 | [Design Twitter](https://leetcode.com/problems/design-twitter/) | M | Merge K feeds |
| [ ] | 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | H | Two heaps ⭐ |
| [ ] | 502 | [IPO](https://leetcode.com/problems/ipo/) | H | Sort + heap |

## My Notes

-
