# 17 · Math & Geometry

> **Prereqs:** 01 · **Time:** 2 days

## When to use

- Matrix manipulation: rotating, spiral traversal, in-place marking.
- Digit manipulation, overflow, modular arithmetic.
- Primes, GCD, fast exponentiation.
- Points, lines and squares on a 2D plane.

## Core concepts

- **Rotate a matrix 90° clockwise** = transpose it, then reverse each row.
- **Spiral order**: shrink the four boundaries (top, bottom, left, right).
- **In-place marking**: use the first row and first column as flags (Set Matrix Zeroes).
- **Fast power**: `x^n` by repeated squaring takes O(log n). Handle negative n.
- **GCD**: `gcd(a, b) = gcd(b, a % b)`. Use it to store a reduced slope `(dy/g, dx/g)` as a hash key (Max Points on a Line).
- **Sieve of Eratosthenes** finds all primes up to n in O(n log log n).
- **Cycle detection on numbers**: use a set or Floyd's algorithm (Happy Number).
- **Modulo** `10**9 + 7`: apply the modulo after every addition or multiplication.
- In Go, C++ or Java, watch for 32-bit **overflow**.

## Templates

```python
# Rotate image
n = len(m)
for i in range(n):
    for j in range(i + 1, n):
        m[i][j], m[j][i] = m[j][i], m[i][j]
for row in m: row.reverse()

# Fast power
def power(x, n):
    if n < 0: x, n = 1 / x, -n
    res = 1
    while n:
        if n & 1: res *= x
        x *= x; n >>= 1
    return res

# Sieve
is_p = [True] * (n + 1); is_p[0:2] = [False, False]
for i in range(2, int(n ** 0.5) + 1):
    if is_p[i]:
        for j in range(i * i, n + 1, i): is_p[j] = False
```

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 66 | [Plus One](https://leetcode.com/problems/plus-one/) | E | Carry |
| [ ] | 202 | [Happy Number](https://leetcode.com/problems/happy-number/) | E | Cycle detection |
| [ ] | 48 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | M | Transpose + reverse ⭐ |
| [ ] | 54 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | M | Shrinking boundaries ⭐ |
| [ ] | 73 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | M | In-place markers |
| [ ] | 50 | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | M | Fast power |
| [ ] | 43 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) | M | Grade-school multiplication |
| [ ] | 204 | [Count Primes](https://leetcode.com/problems/count-primes/) | M | Sieve |
| [ ] | 2013 | [Detect Squares](https://leetcode.com/problems/detect-squares/) | M | Diagonal-point counting |
| [ ] | 149 | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) | H | GCD slope key |

## My Notes

-
