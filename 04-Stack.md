# 04 · Stack & Monotonic Stack

> **Prereqs:** 01 · **Time:** 3 days

## When to use

- Matching or nesting: parentheses, tags, decoding strings like `3[a2[c]]`.
- Expression evaluation (RPN, calculators).
- **"Next greater or smaller element"** and "how far until a warmer day": use a **monotonic stack**.
- "Largest rectangle" or "span" problems.
- Undo operations, or emulating recursion iteratively.

## Core concepts

- LIFO, with O(1) push, pop and peek.
- **Monotonic stack**: keeps elements in increasing or decreasing order. When a new element breaks the order, pop the stack. Each popped element has just found its "next greater or smaller" element.
  - Use a decreasing stack to find the next **greater** element, and an increasing stack to find the next **smaller** one.
- Store **indices** rather than values so you can calculate distances and widths.
- Min stack: store the pair `(value, current_min)` at each level.

## Templates

```python
# Next greater element (to the right)
res = [-1] * n
st = []  # indices, values decreasing
for i, x in enumerate(nums):
    while st and nums[st[-1]] < x:
        res[st.pop()] = x
    st.append(i)

# Circular variant: iterate 2n, index i % n

# Largest rectangle in histogram
st, best = [], 0
for i, h in enumerate(heights + [0]):
    start = i
    while st and st[-1][1] > h:
        idx, ht = st.pop()
        best = max(best, ht * (i - idx))
        start = idx
    st.append((start, h))
```

## Pitfalls

- Popping from an empty stack. Always check `while st and ...`.
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
