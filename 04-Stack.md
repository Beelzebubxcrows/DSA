# 04 · Stack & Monotonic Stack

> **Prereqs:** 01 · **Time:** 3 days

## When to use

- Matching or nesting: parentheses, tags, decoding strings like `3[a2[c]]`.
- Expression evaluation (RPN, calculators).
- **"Next greater or smaller element"** and "how far until a warmer day": use a **monotonic stack**.
- "Largest rectangle" or "span" problems.
- Undo operations, or emulating recursion iteratively.

## Core concepts

- LIFO, with O(1) push, pop and peek. In Java, use `Deque<Integer> st = new ArrayDeque<>()` with `push`, `pop` and `peek`. Avoid the old `Stack` class, which is synchronized and slower.
- **Monotonic stack**: keeps elements in increasing or decreasing order. When a new element breaks the order, pop the stack. Each popped element has just found its "next greater or smaller" element.
  - Use a decreasing stack to find the next **greater** element, and an increasing stack to find the next **smaller** one.
- Store **indices** rather than values so you can calculate distances and widths.
- Min stack: store the pair `int[]{value, currentMin}` at each level.

## Templates

```java
// Next greater element (to the right)
int[] res = new int[n];
Arrays.fill(res, -1);
Deque<Integer> st = new ArrayDeque<>();   // indices, values decreasing
for (int i = 0; i < n; i++) {
    while (!st.isEmpty() && nums[st.peek()] < nums[i])
        res[st.pop()] = nums[i];
    st.push(i);
}

// Circular variant: iterate i from 0 to 2n - 1, use i % n

// Largest rectangle in histogram
Deque<Integer> st = new ArrayDeque<>();   // indices, heights increasing
int best = 0;
for (int i = 0; i <= heights.length; i++) {
    int h = i == heights.length ? 0 : heights[i];   // sentinel 0 empties the stack
    while (!st.isEmpty() && heights[st.peek()] > h) {
        int height = heights[st.pop()];
        int left = st.isEmpty() ? -1 : st.peek();
        best = Math.max(best, height * (i - left - 1));
    }
    st.push(i);
}
```

## Pitfalls

- Popping from an empty stack. `pop()` on an empty `ArrayDeque` throws, so always check `!st.isEmpty() && ...`.
- `ArrayDeque` doesn't accept `null`.
- Elements left on the stack at the end need handling. Use a sentinel value or a post-processing step.
- Deciding between strict and non-strict comparison (`<` vs `<=`) when values are duplicated.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | E | Matching |
| [ ] | 232 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | E | Two stacks, amortized |
| [ ] | 496 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | E | Monotonic |
| [ ] | 155 | [Min Stack](https://leetcode.com/problems/min-stack/) | M | Pair (value, min) |
| [ ] | 150 | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | M | Operand stack |
| [ ] | 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | M | Monotonic decreasing |
| [ ] | 503 | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) | M | Circular, 2n pass |
| [ ] | 394 | [Decode String](https://leetcode.com/problems/decode-string/) | M | Stack of (string, count) |
| [ ] | 853 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | M | Sort + stack of times |
| [ ] | 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | H | Monotonic increasing |
| [ ] | 224 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | H | Sign stack |

## My Notes

-
