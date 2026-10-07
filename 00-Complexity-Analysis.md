# 00 · Complexity Analysis

> **Goal:** be able to state the time and space complexity of any solution right away, and use the constraints to work out which complexity is expected.

## Core concepts

- **Big-O** gives an upper bound on growth. Drop constants and lower-order terms: `O(3n² + n)` becomes `O(n²)`.
- **Time complexity** counts the dominant operations as the input size grows.
- **Space complexity** counts the extra memory used, *including the recursion stack*.
- **Amortized complexity** is the average cost over a sequence of operations. Appending to a dynamic array is amortized `O(1)` even though an occasional resize costs `O(n)`.
- **Best, average and worst case.** Quicksort is `O(n log n)` on average and `O(n²)` in the worst case. Hash maps are `O(1)` on average and `O(n)` in the worst case.

## Common complexities (fastest to slowest)

| Complexity | Typical source |
|------------|----------------|
| O(1) | Hash lookup, array index |
| O(log n) | Binary search, operations on a balanced tree or heap |
| O(n) | Single pass over the input |
| O(n log n) | Sorting, n heap operations |
| O(n²) | Nested loops, 2D DP over n×n |
| O(2ⁿ) | Subsets, naive recursion |
| O(n!) | Permutations |

## Constraint → target complexity (very useful)

A computer does roughly 10⁸ simple operations per second. Use n to work out which approach is expected:

| n up to | Target | Likely approach |
|---------|--------|-----------------|
| ≤ 10–12 | O(n!) | Permutations, brute force |
| ≤ 20–25 | O(2ⁿ) | Subsets, bitmask, backtracking |
| ≤ 500 | O(n³) | Interval DP, Floyd–Warshall |
| ≤ 5,000 | O(n²) | 2D DP, nested loops |
| ≤ 10⁵ – 10⁶ | O(n log n) / O(n) | Sort, heap, binary search, two pointers, hashing |
| ≥ 10⁹ | O(log n) / O(1) | Binary search on the answer, math |

## Recursion complexity

- **Time** = (number of calls) × (work per call). For a recursion tree, multiply the branching factor raised to the depth by the work done at each node.
- **Space** = maximum recursion depth plus any extra structures.
- **Master theorem (quick version):** `T(n) = aT(n/b) + O(n^d)`
  - if `d > log_b a`, the answer is `O(n^d)`
  - if `d = log_b a`, the answer is `O(n^d log n)`. Merge sort is `2T(n/2)+O(n)`, which gives `O(n log n)`.
  - if `d < log_b a`, the answer is `O(n^(log_b a))`

## Built-in operation costs (Python)

| Operation | Cost |
|-----------|------|
| `list.append`, `list.pop()` | O(1) |
| `list.pop(0)`, `list.insert(0, x)`, `x in list` | O(n). Use `collections.deque` instead. |
| `dict` / `set` get, set, `in` | O(1) average |
| `sorted()` / `.sort()` | O(n log n) |
| `heapq.heappush` / `heappop` | O(log n) |
| `heapq.heapify` | O(n) |
| String concatenation in a loop | O(n²) overall. Use `''.join(parts)`. |
| Slicing `a[i:j]` | O(j - i) |

## Pitfalls

- Forgetting to count recursion stack space.
- Calling `x in list` inside a loop, which silently makes it O(n²).
- Treating string slicing or copying as O(1).
- Using sorting when O(n) is expected.

## Practice

There are no specific problems for this topic. State the complexity of every problem you solve in the other topics.

## My Notes

-
