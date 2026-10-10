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
| Power of two? | `x > 0 && (x & (x - 1)) == 0` |
| Count set bits | `Integer.bitCount(x)` or Kernighan's loop |
| Iterate all subsets of n items | `for (int mask = 0; mask < (1 << n); mask++)` |
| Counting bits DP | `bits[i] = bits[i >> 1] + (i & 1)` |

## Java gotchas

- `int` is 32-bit two's complement and overflow wraps silently. Use `long` and `1L << i` when you need bit 31 or higher.
- `>>` is an arithmetic shift (copies the sign bit). `>>>` is a logical shift (fills with 0). Use `>>>` when treating an `int` as unsigned, as in Number of 1 Bits and Reverse Bits.
- `==` binds tighter than `&`, `|` and `^`. Write `(x & 1) == 1`. Without the parentheses it doesn't compile.
- Shift counts are taken mod 32 (mod 64 for `long`), so `1 << 32 == 1`.
- Because `int` already wraps at 32 bits, Sum of Two Integers needs no masking in Java.

## Templates

```java
// Single number
int res = 0;
for (int x : nums) res ^= x;

// Kernighan popcount
int cnt = 0;
while (x != 0) {
    x &= x - 1;
    cnt++;
}

// Sum without + (int wraps at 32 bits, so negatives just work)
while (b != 0) {
    int carry = (a & b) << 1;
    a ^= b;
    b = carry;
}
return a;
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
