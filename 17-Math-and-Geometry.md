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
- **Modulo** `1_000_000_007`: apply the modulo after every addition or multiplication, and multiply as `long`: `(long) a * b % MOD`.
- Java's `%` keeps the sign of the left operand, so `-7 % 3 == -1`. Use `((a % m) + m) % m` for a non-negative result.
- Watch for 32-bit `int` **overflow**: use `long` for products and large sums. `Math.addExact` / `Math.multiplyExact` throw instead of silently wrapping.

## Templates

```java
// Rotate image
int n = m.length;
for (int i = 0; i < n; i++)
    for (int j = i + 1; j < n; j++) {
        int t = m[i][j]; m[i][j] = m[j][i]; m[j][i] = t;
    }
for (int[] row : m)
    for (int l = 0, r = n - 1; l < r; l++, r--) {
        int t = row[l]; row[l] = row[r]; row[r] = t;
    }

// Fast power
double power(double x, long n) {   // long: negating Integer.MIN_VALUE overflows int
    if (n < 0) { x = 1 / x; n = -n; }
    double res = 1;
    while (n > 0) {
        if ((n & 1) == 1) res *= x;
        x *= x;
        n >>= 1;
    }
    return res;
}

// Sieve
boolean[] isPrime = new boolean[n + 1];
for (int i = 2; i <= n; i++) isPrime[i] = true;
for (int i = 2; (long) i * i <= n; i++)
    if (isPrime[i])
        for (int j = i * i; j <= n; j += i) isPrime[j] = false;
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
