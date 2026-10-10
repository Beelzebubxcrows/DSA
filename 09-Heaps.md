# 09 · Heaps / Priority Queue

> **Prereqs:** 01 · **Time:** 2–3 days

## When to use

- "Top K", "Kth largest or smallest", "K closest".
- Repeatedly taking the min or max as the data changes (scheduling, simulations).
- Merging K sorted lists or streams.
- **Median of a stream**: use two heaps.
- Dijkstra's algorithm and Prim's algorithm (topic 12).

## Core concepts

- A binary heap gives O(log n) push and pop and O(1) peek. Building one from a whole collection (`new PriorityQueue<>(list)`) takes O(n).
- Java's `PriorityQueue` is a **min-heap** by default. For a max-heap, use `new PriorityQueue<>(Collections.reverseOrder())`.
- **Top K largest**: keep a **min-heap of size K**. This takes O(n log k).
- For pairs or objects, pass a comparator, e.g. `new PriorityQueue<int[]>((a, b) -> Integer.compare(a[0], b[0]))`.
- **Two heaps for the median**: a max-heap holds the lower half and a min-heap holds the upper half. Keep their sizes within 1 of each other.
- **Quickselect** finds the Kth element in O(n) on average. It's a good optimisation to mention.

## Templates

```java
// K largest with min-heap of size k
PriorityQueue<Integer> h = new PriorityQueue<>();
for (int x : nums) {
    h.offer(x);
    if (h.size() > k) h.poll();
}
return h.peek();   // kth largest

// Max-heap
PriorityQueue<Integer> maxH = new PriorityQueue<>(Collections.reverseOrder());

// Merge k sorted lists
PriorityQueue<ListNode> h = new PriorityQueue<>((a, b) -> Integer.compare(a.val, b.val));
for (ListNode node : lists) if (node != null) h.offer(node);
ListNode dummy = new ListNode(), tail = dummy;
while (!h.isEmpty()) {
    ListNode node = h.poll();
    tail.next = node;
    tail = node;
    if (node.next != null) h.offer(node.next);
}

// Two heaps median
PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder());   // lower half, max-heap
PriorityQueue<Integer> hi = new PriorityQueue<>();                             // upper half, min-heap
void add(int x) {
    lo.offer(x);
    hi.offer(lo.poll());
    if (hi.size() > lo.size()) lo.offer(hi.poll());
}
double median() {
    return lo.size() > hi.size() ? lo.peek() : ((double) lo.peek() + hi.peek()) / 2;
}
```

## Pitfalls

- Adding arrays or custom objects without a comparator, which throws `ClassCastException`.
- Writing the comparator as `(a, b) -> b - a`. It overflows for large or negative values. Use `Integer.compare(b, a)` or `Collections.reverseOrder()`.
- Iterating over a `PriorityQueue` (or printing it) doesn't give sorted order. Only repeated `poll()` does.
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
