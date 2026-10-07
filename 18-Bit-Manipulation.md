# 18 · Bit Manipulation

> **Prereqs:** none · **Time:** 1–2 days

## When to use

- "Every element appears twice except one" (XOR).
- O(1) space is required for counting or finding elements.
- Representing subsets compactly (bitmask DP, n ≤ 20).
- Arithmetic without using `+` or `*`.

## Core tricks

| Trick | Expression |
|-------|-----------|
| XOR cancels pairs | `a ^ a = 0`, `a ^ 0 = a` |
| Check bit i | `(x >> i) & 1` |
| Set / clear / toggle bit i | `x \| (1<<i)`, `x & ~(1<<i)`, `x ^ (1<<i)` |
| Clear lowest set bit | `x & (x - 1)` |
| Isolate lowest set bit | `x & -x` |
| Power of two? | `x > 0 and x & (x - 1) == 0` |
| Count set bits | `bin(x).count('1')` or Kernighan's loop |
| Iterate all subsets of n items | `for mask in range(1 << n)` |
| Counting bits DP | `bits[i] = bits[i >> 1] + (i & 1)` |

## Python gotchas

- Python integers have unlimited size, so negative numbers don't wrap. To simulate 32-bit integers, use `mask = 0xFFFFFFFF`, and if the result is greater than `0x7FFFFFFF`, convert it with `~(res ^ mask)`.
- `>>` on a negative number is an arithmetic shift.

## Templates

```python
# Single number
res = 0
for x in nums: res ^= x

# Kernighan popcount
cnt = 0
while x:
    x &= x - 1; cnt += 1

# Sum without + (32-bit simulation)
MASK = 0xFFFFFFFF
while b & MASK:
    a, b = a ^ b, (a & b) << 1
return a & MASK if b > 0 else a  # (see editorial for full sign handling)
```

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 136 | [Single Number](https://leetcode.com/problems/single-number/) | E | XOR |
| [ ] | 191 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | E | Kernighan |
| [ ] | 338 | [Counting Bits](https://leetcode.com/problems/counting-bits/) | E | DP on bits |
| [ ] | 190 | [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | E | Shift and build |
| [ ] | 268 | [Missing Number](https://leetcode.com/problems/missing-number/) | E | XOR with indices |
| [ ] | 371 | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | M | XOR + carry |
| [ ] | 7 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/) | M | Overflow check |
| [ ] | 137 | [Single Number II](https://leetcode.com/problems/single-number-ii/) | M | Count each bit mod 3 |
| [ ] | 260 | [Single Number III](https://leetcode.com/problems/single-number-iii/) | M | Split on the lowest set bit |
| [ ] | 201 | [Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) | M | Common prefix |

## My Notes

-
