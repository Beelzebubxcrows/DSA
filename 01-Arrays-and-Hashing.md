# 01 · Arrays & Hashing

> **Prereqs:** 00 · **Time:** 7–8 days · **Sources:** NeetCode 150/250, Striver A2Z + SDE sheet, Love Babbar 450, LeetCode Discuss FAANG threads

Work through the subtopics in order. Each one has an explanation, a worked example, a Java template, further reading and its questions (Easy, then Medium, then Hard). Then use **Misc** as a mixed self-test, where the pattern isn't given away by the heading.

## When to use

- "Have I seen this before?", "count occurrences", "find the pair or complement": use a **hash map or set**.
- "Sum or count of a subarray", especially with negative numbers: use **prefix sums**, often combined with a hash map.
- "Maximum sum of a contiguous subarray": use **Kadane's algorithm**.
- Grouping items by a property (anagrams, for example): use a **hash map with a canonical key**.
- "Top K most frequent" with frequencies bounded by n: use **bucket sort**.
- "Element appearing more than n/2 (or n/3) times" in O(1) space: use **Boyer-Moore voting**.
- Values in the range `1..n` and O(1) extra space: use **index as hash**, either cyclic sort or sign marking.
- Sorting an array with only 2 or 3 distinct kinds of values in one pass: use **Dutch national flag** partitioning.

## Subtopics at a glance

| # | Subtopic | Key idea | Typical cost |
|---|----------|----------|--------------|
| 1 | Array manipulation | Reverse, rotate, scan from the right | O(n) time, O(1) space |
| 2 | Hashing: sets and maps | Trade O(n) memory for O(1) lookups | O(n) time, O(n) space |
| 3 | Top K and bucket sort | Index the buckets by frequency | O(n) |
| 4 | Prefix sums | `sum(l..r) = pre[r+1] - pre[l]`, with a map of earlier prefixes | O(n) |
| 5 | Kadane's algorithm | Extend the current subarray, or restart | O(n), O(1) |
| 6 | Boyer-Moore voting | Pairs of different values cancel out | O(n), O(1) |
| 7 | Index as hash | Value v belongs at index v − 1 | O(n), O(1) |
| 8 | Partitioning | Three pointers: low, mid, high | O(n), O(1) |
| 9 | Sorting tricks and merge-sort counting | Sort first, or count pairs during merging | O(n log n) |
| 10 | Design with hashing | Map plus list or array | O(1) per operation |

## 1. Array manipulation

### About

These are the building blocks that FAANG warm-up questions and the Striver/Babbar "easy" sections test: traversal, in-place rotation, scanning from the right, and building the next arrangement. The trick is usually to avoid an extra array by **reversing** parts of the input or **scanning in the right direction**.

- **Rotate by k**: reverse the whole array, then reverse each part. This is O(1) space.
- **Leaders / greatest to the right**: scan from the right and track the maximum so far.
- **Next permutation**: find the first "dip" from the right, swap it with the smallest larger value to its right, then reverse the suffix.

### Example

Rotate `[1,2,3,4,5,6,7]` right by `k = 3`:
1. Reverse everything: `[7,6,5,4,3,2,1]`
2. Reverse the first k: `[5,6,7,4,3,2,1]`
3. Reverse the rest: `[5,6,7,1,2,3,4]` ✅

Next permutation of `[1,3,5,4,2]`: the first dip from the right is `3` (because `3 < 5`). The smallest value to its right that's bigger than 3 is `4`. Swap them to get `[1,4,5,3,2]`, then reverse the suffix after index 1 to get `[1,4,2,3,5]`.

### Template

```java
// Rotate right by k with three reversals
k %= n;
reverse(a, 0, n - 1);
reverse(a, 0, k - 1);
reverse(a, k, n - 1);

// Leaders: scan from the right, tracking the max so far
int maxRight = Integer.MIN_VALUE;
for (int i = n - 1; i >= 0; i--) {
    if (a[i] > maxRight) leaders.add(a[i]);
    maxRight = Math.max(maxRight, a[i]);
}

// Next permutation
int i = n - 2;
while (i >= 0 && a[i] >= a[i + 1]) i--;   // 1. first dip from the right
if (i >= 0) {
    int j = n - 1;
    while (a[j] <= a[i]) j--;             // 2. smallest value on the right that's bigger than a[i]
    swap(a, i, j);
}
reverse(a, i + 1, n - 1);                 // 3. make the suffix as small as possible
```

### Read more

- [Next lexicographical permutation algorithm (Nayuki)](https://www.nayuki.io/page/next-lexicographical-permutation-algorithm): the clearest illustrated explanation.
- [Permutation: generation in lexicographic order (Wikipedia)](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | E | Warm-up |
| [ ] | 414 | [Third Maximum Number](https://leetcode.com/problems/third-maximum-number/) | E | Track the top 3 in one pass |
| [ ] | 1752 | [Check if Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/) | E | Count the drops (at most 1) |
| [ ] | 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | E | Running count |
| [ ] | 1299 | [Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/) | E | Scan from the right (leaders) |
| [ ] | 118 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | E | Build each row from the previous one |
| [ ] | 189 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | M | Three reversals |
| [ ] | 2149 | [Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/) | M | Two write indices (even/odd) |
| [ ] | 31 | [Next Permutation](https://leetcode.com/problems/next-permutation/) | M | Dip, swap, reverse suffix ⭐ |

## 2. Hashing: sets and maps

### About

A `HashSet` answers "have I seen x?" in O(1) on average, and a `HashMap` answers "how many times, or where, have I seen x?". Most O(n²) brute-force pair checks become O(n) once you store what you've already seen.

- **Complement lookup**: for each x, check whether `target - x` has been seen *before* it.
- **Frequency counting**: `int[26]` for lowercase letters (faster, with no boxing), otherwise `map.merge(x, 1, Integer::sum)`.
- **Canonical key**: map every item to a key that's equal for items in the same group (sorted letters, a count signature, a row tuple).
- **Bijection checks** (isomorphic strings, word pattern): use two maps, one for each direction.

### Example

Two Sum, with `nums = [2,7,11,15]` and `target = 9`:
- i = 0: we need 7, which we haven't seen. Store `2 → 0`.
- i = 1: we need 2, and we've seen it at index 0. The answer is `[0, 1]`.

Longest Consecutive Sequence, with `[100,4,200,1,3,2]`: put everything in a set. Only start counting from numbers whose `x − 1` is *not* in the set (here, 1, 100 and 200). Counting up from 1 finds 1, 2, 3, 4, a length of 4. Each number is visited at most twice, so this is O(n).

### Template

```java
// Frequency count (lowercase letters)
int[] cnt = new int[26];
for (char c : s.toCharArray()) cnt[c - 'a']++;

// Frequency count (general keys)
Map<Integer, Integer> freq = new HashMap<>();
for (int x : nums) freq.merge(x, 1, Integer::sum);

// Complement lookup (Two Sum)
Map<Integer, Integer> seen = new HashMap<>();
for (int i = 0; i < nums.length; i++) {
    Integer j = seen.get(target - nums[i]);
    if (j != null) return new int[]{j, i};
    seen.put(nums[i], i);
}

// Longest consecutive: only count from the start of a run
Set<Integer> set = new HashSet<>();
for (int x : nums) set.add(x);
int best = 0;
for (int x : set) {
    if (set.contains(x - 1)) continue;   // not the start of a run
    int len = 1;
    while (set.contains(x + len)) len++;
    best = Math.max(best, len);
}

// Canonical key grouping (anagrams)
Map<String, List<String>> groups = new HashMap<>();
for (String w : words) {
    char[] cs = w.toCharArray();
    Arrays.sort(cs);
    groups.computeIfAbsent(new String(cs), x -> new ArrayList<>()).add(w);
}
```

### Read more

- [Hash table (Wikipedia)](https://en.wikipedia.org/wiki/Hash_table): collisions, load factor, and why the worst case is O(n).
- [`HashMap` Javadoc](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/HashMap.html): `merge`, `computeIfAbsent`, `getOrDefault`.
- [Highest frequency element (takeUforward)](https://takeuforward.org/blogs/data-structure-and-algorithm/highest-freq-element): Striver's hashing intro.

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | E | Set |
| [ ] | 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | E | Counting |
| [ ] | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | E | Complement map ⭐ |
| [ ] | 349 | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | E | Set intersection |
| [ ] | 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | E | Count, then scan |
| [ ] | 205 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | E | Two-way mapping |
| [ ] | 290 | [Word Pattern](https://leetcode.com/problems/word-pattern/) | E | Two-way mapping |
| [ ] | 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | M | Canonical key ⭐ |
| [ ] | 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | M | Sets per row/col/box |
| [ ] | 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | M | Set, start of sequence ⭐ |
| [ ] | 532 | [K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) | M | Count map, look up x + k |
| [ ] | 1010 | [Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/) | M | Complement of remainders |
| [ ] | 454 | [4Sum II](https://leetcode.com/problems/4sum-ii/) | M | Meet in the middle with a map |
| [ ] | 554 | [Brick Wall](https://leetcode.com/problems/brick-wall/) | M | Count the edge positions |

## 3. Top K and bucket sort

### About

Sorting by frequency costs O(n log n). Because a frequency can never exceed n, you can instead make an array of **n + 1 buckets indexed by frequency** and read it from the top. This is O(n). A heap (topic 09) is the alternative when you need streaming or lexicographic tie-breaks. Counting sort uses the same "bounded values" idea, as in H-Index.

### Example

`nums = [1,1,1,2,2,3]`, `k = 2`. The frequencies are `{1:3, 2:2, 3:1}`, so `buckets[3] = [1]`, `buckets[2] = [2]` and `buckets[1] = [3]`. Reading from the top gives `[1, 2]`.

### Template

```java
// Top K frequent with bucket sort: index = frequency
Map<Integer, Integer> freq = new HashMap<>();
for (int x : nums) freq.merge(x, 1, Integer::sum);
List<List<Integer>> buckets = new ArrayList<>();
for (int f = 0; f <= nums.length; f++) buckets.add(new ArrayList<>());
freq.forEach((x, f) -> buckets.get(f).add(x));
int[] res = new int[k];
int i = 0;
for (int f = nums.length; f > 0 && i < k; f--)
    for (int x : buckets.get(f))
        if (i < k) res[i++] = x;
```

### Read more

- [Bucket sort (Wikipedia)](https://en.wikipedia.org/wiki/Bucket_sort)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | M | Bucket sort / heap ⭐ |
| [ ] | 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | M | Bucket sort |
| [ ] | 692 | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | M | Heap with tie-break on the word |
| [ ] | 274 | [H-Index](https://leetcode.com/problems/h-index/) | M | Counting sort, capped at n |

## 4. Prefix sums

### About

Precompute `pre[i] = a[0] + … + a[i-1]` once, and any range sum becomes `pre[r+1] − pre[l]` in O(1). Combined with a hash map of the prefixes seen so far, "count or find subarrays with sum k" becomes O(n), **and it works with negative numbers**, unlike a sliding window.

- **Count subarrays with sum k**: map each prefix to how many times it has occurred, and seed it with `{0: 1}`.
- **Longest subarray with sum k**: map each prefix to its **first** index, and seed it with `{0: -1}`.
- **Divisible by k**: use `((sum % k) + k) % k` as the key, because Java's `%` can be negative.
- **Equal numbers of 0s and 1s**: replace each 0 with −1, and the question becomes "longest subarray with sum 0".
- **Product except self**: a prefix-product pass, then a suffix-product pass, with no division.
- **2D**: `P[r+1][c+1] = a[r][c] + P[r][c+1] + P[r+1][c] − P[r][c]` (inclusion–exclusion).

### Example

`nums = [1,2,3]`, `k = 3`. The running prefix goes 1, 3, 6.
- At prefix 1, we need 1 − 3 = −2. It hasn't been seen, so nothing is added.
- At prefix 3, we need 0. It has been seen once (the seed), so the count becomes 1 (that's `[1,2]`).
- At prefix 6, we need 3. It has been seen once, so the count becomes 2 (that's `[3]`). The answer is **2**.

### Template

```java
// Build prefix sums: pre[i] = sum of a[0..i-1]
int[] pre = new int[n + 1];
for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + a[i];
// sum(a[l..r]) = pre[r + 1] - pre[l]

// Count subarrays with sum == k (works with negatives)
Map<Integer, Integer> pref = new HashMap<>();
pref.put(0, 1);
int count = 0, sum = 0;
for (int x : nums) {
    sum += x;
    count += pref.getOrDefault(sum - k, 0);
    pref.merge(sum, 1, Integer::sum);
}

// Longest subarray with sum == k: store the FIRST index of each prefix
Map<Integer, Integer> first = new HashMap<>();
first.put(0, -1);
int sum = 0, best = 0;
for (int i = 0; i < n; i++) {
    sum += a[i];
    if (first.containsKey(sum - k)) best = Math.max(best, i - first.get(sum - k));
    first.putIfAbsent(sum, i);
}

// Product of array except self: prefix pass, then suffix pass
int[] res = new int[n];
res[0] = 1;
for (int i = 1; i < n; i++) res[i] = res[i - 1] * a[i - 1];
int suffix = 1;
for (int i = n - 1; i >= 0; i--) {
    res[i] *= suffix;
    suffix *= a[i];
}
```

### Read more

- [Prefix sum (Wikipedia)](https://en.wikipedia.org/wiki/Prefix_sum)
- [Hashing and Prefix Sum: Definitive Guide (LeetCode Discuss)](https://leetcode.com/discuss/study-guide/4781120/Hashing-and-Prefix-Sum-:-Definitive-Guide/)
- [Prefix sum study summary (LeetCode Discuss)](https://leetcode.com/discuss/study-guide/2719912/Prefix-sum-study-summary/): problems grouped by use case.
- [Subarray Sum Patterns (LeetCode Discuss)](https://leetcode.com/discuss/post/5284478/Subarray-Sum-Patterns/)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | E | Prefix sum |
| [ ] | 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | E | Left sum vs total − left − a[i] |
| [ ] | 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | M | Prefix & suffix ⭐ |
| [ ] | 304 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | M | 2D prefix sum |
| [ ] | 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | M | Prefix sum + count map ⭐ |
| [ ] | 325 | [Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) 🔒 | M | Prefix sum + first-index map |
| [ ] | 525 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | M | 0 → −1, longest sum 0 |
| [ ] | 523 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | M | Prefix mod k, first index |
| [ ] | 974 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | M | Prefix mod k, count map |

## 5. Kadane's algorithm

### About

The best subarray **ending at i** either extends the best one ending at i − 1 or starts fresh at i: `cur = max(a[i], cur + a[i])`. Track the best value seen overall. It's the most-asked array DP in Indian product-company and FAANG screens, and Babbar marks it "V.V. IMP".

- **Return the subarray too**: reset `start` whenever `cur` drops to 0 or below before adding a[i].
- **Circular array**: the answer is `max(normal Kadane, total − minimum subarray)`. If every number is negative, return the normal Kadane result.
- **Product instead of sum**: track both the max and the min, because a negative times a negative flips them. That's topic 13 (Maximum Product Subarray).

### Example

`[-2,1,-3,4,-1,2,1,-5,4]`: `cur` goes −2, 1, −2, **4, 3, 5, 6**, 1, 5. The best is **6**, from `[4,-1,2,1]`.

### Template

```java
// Kadane: extend or restart
int best = nums[0], cur = nums[0];
for (int i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i]);
    best = Math.max(best, cur);
}

// Kadane returning the subarray boundaries
int best = Integer.MIN_VALUE, cur = 0, start = 0, bestL = 0, bestR = 0;
for (int i = 0; i < n; i++) {
    if (cur <= 0) { cur = 0; start = i; }
    cur += a[i];
    if (cur > best) { best = cur; bestL = start; bestR = i; }
}
```

### Read more

- [Search the subsegment with the maximum/minimum sum (cp-algorithms)](https://cp-algorithms.com/others/maximum_average_segment.html): both the prefix-sum and Kadane views.
- [Maximum subarray problem (Wikipedia)](https://en.wikipedia.org/wiki/Maximum_subarray_problem)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | M | Kadane ⭐ |
| [ ] | 918 | [Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/) | M | max(Kadane, total − min subarray) |

## 6. Boyer-Moore voting

### About

If one value appears more than n/2 times, cancelling each occurrence against a *different* value always leaves it standing. That gives O(n) time and O(1) space, without a hash map. For "more than n/3", keep **two** candidates (in general, k − 1 candidates for n/k), then **verify** them with a second pass, because the cancellation only produces candidates.

### Example

`[2,2,1,1,1,2,2]`:

| x | 2 | 2 | 1 | 1 | 1 | 2 | 2 |
|---|---|---|---|---|---|---|---|
| candidate | 2 | 2 | 2 | 2 | 1 | 1 | 2 |
| count | 1 | 2 | 1 | 0 | 1 | 0 | 1 |

At the fifth element the count is 0, so the candidate becomes 1. The next 2 cancels it back to 0, so the last element makes 2 the candidate again. The answer is **2**.

### Template

```java
// Boyer-Moore voting (majority > n/2 guaranteed)
int cand = 0, count = 0;
for (int x : nums) {
    if (count == 0) cand = x;
    count += (x == cand) ? 1 : -1;
}
return cand;

// Extended voting (> n/3): two candidates, then verify
int c1 = 0, c2 = 1, n1 = 0, n2 = 0;   // start with two different values
for (int x : nums) {
    if (x == c1) n1++;
    else if (x == c2) n2++;
    else if (n1 == 0) { c1 = x; n1 = 1; }
    else if (n2 == 0) { c2 = x; n2 = 1; }
    else { n1--; n2--; }
}
// second pass: count c1 and c2, keep each one whose count is > n / 3
```

### Read more

- [Boyer–Moore majority vote algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
- [Majority Element, n/2 (takeUforward)](https://takeuforward.org/blogs/data-structure-and-algorithm/majority-element-n-by-2)
- [Majority Element II, n/3 (takeUforward)](https://takeuforward.org/blogs/data-structure-and-algorithm/majority-element-ii-n-by-3): brute force, then hashing, then voting, plus the n/k generalisation.

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 169 | [Majority Element](https://leetcode.com/problems/majority-element/) | E | Boyer-Moore |
| [ ] | 229 | [Majority Element II](https://leetcode.com/problems/majority-element-ii/) | M | Two candidates + verify ⭐ |

## 7. Index as hash (cyclic sort and sign marking)

### About

When the values are in `1..n` and the problem asks for missing or duplicate numbers in O(1) extra space, **the array itself is the hash table**: value `v` belongs at index `v − 1`.

- **Cyclic sort**: keep swapping `a[i]` into its home slot until slot i holds the right value or an unusable one. Every swap places one value permanently, so the whole thing is O(n).
- **Sign marking**: to record that v was seen, negate `a[v − 1]`. Use `Math.abs` when reading values, because they may already be negative.

### Example

First Missing Positive, with `[3,4,-1,1]`. Cyclic sort moves 3 to index 2, 4 to index 3 and 1 to index 0, which gives `[1,-1,3,4]`. Index 1 doesn't hold 2, so the answer is **2**.

### Template

```java
// Cyclic sort: put each value v in 1..n at index v - 1
for (int i = 0; i < n; ) {
    int v = a[i];
    if (v >= 1 && v <= n && a[v - 1] != v) { a[i] = a[v - 1]; a[v - 1] = v; }
    else i++;
}
// afterwards, the first i with a[i] != i + 1 means i + 1 is missing (and a[i] is a duplicate)

// Sign marking: record "v seen" by negating a[v - 1]
for (int x : a) {
    int idx = Math.abs(x) - 1;
    if (a[idx] < 0) duplicates.add(idx + 1);
    else a[idx] = -a[idx];
}
```

### Read more

- [Cycle sort (Wikipedia)](https://en.wikipedia.org/wiki/Cycle_sort)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 448 | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | E | Sign marking |
| [ ] | 645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/) | E | Repeating + missing (index as hash or math) |
| [ ] | 442 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | M | Sign marking |
| [ ] | 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | H | Cyclic sort ⭐ |

## 8. Partitioning (Dutch national flag)

### About

Rearrange the array in place into groups (less than, equal to, greater than a pivot, or 0s, 1s and 2s) in **one pass**. Keep three regions: `[0, lo)` is done-low, `[lo, mid)` is done-middle, and `(hi, n−1]` is done-high. `[mid, hi]` is still unknown. Quicksort's 3-way partition uses the same loop.

### Example

`[2,0,2,1,1,0]`: swap the 2 to the back, pull the 0s to the front and step over the 1s. The result is `[0,0,1,1,2,2]`. Every element is looked at once.

### Template

```java
// Dutch national flag: [0..lo) = 0s, [lo..mid) = 1s, (hi..n-1] = 2s
int lo = 0, mid = 0, hi = n - 1;
while (mid <= hi) {
    if (a[mid] == 0) swap(a, lo++, mid++);
    else if (a[mid] == 1) mid++;
    else swap(a, mid, hi--);   // don't advance mid: the value swapped in hasn't been checked yet
}
```

### Read more

- [Dutch national flag problem (Wikipedia)](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 905 | [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/) | E | Two-way partition |
| [ ] | 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | M | Dutch national flag ⭐ |
| [ ] | 2161 | [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/) | M | Stable 3-way partition |

## 9. Sorting tricks and merge-sort counting

### About

- **Sort first**: once the array is sorted, "the closest k values" become a window of k neighbours (Babbar's chocolate distribution), and "add or subtract K from each height" becomes a single split point (Babbar's minimise the heights).
- **Count pairs during merge sort**: to count pairs `i < j` with `a[i] > a[j]` (inversions) or `a[i] > 2·a[j]` (reverse pairs), count across the two sorted halves before merging them. This takes O(n log n). It's Striver's "hard arrays" favourite.

### Example

Reverse Pairs, with `[1,3,2,3,1]`: the pairs are (3 at index 1, 1 at index 4) and (3 at index 3, 1 at index 4), so the answer is **2**. When the two halves are merged, both 3s in the left half see the 1 in the right half.

### Template

```java
// Count pairs i < j with a[i] > 2 * a[j] using merge sort (Reverse Pairs)
int sortCount(int[] a, int lo, int hi) {   // sorts a[lo..hi] and returns the pair count
    if (lo >= hi) return 0;
    int mid = (lo + hi) >>> 1;
    int count = sortCount(a, lo, mid) + sortCount(a, mid + 1, hi);
    for (int i = lo, j = mid + 1; i <= mid; i++) {   // both halves are sorted here
        while (j <= hi && a[i] > 2L * a[j]) j++;
        count += j - (mid + 1);
    }
    merge(a, lo, mid, hi);   // standard merge of the two sorted halves
    return count;
}
// For inversions, use a[i] > a[j] in the counting loop.
```

### Read more

- [Inversion (Wikipedia)](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 1984 | [Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/) | E | Sort + window of k (chocolate distribution) |
| [ ] | 910 | [Smallest Range II](https://leetcode.com/problems/smallest-range-ii/) | M | Sort + try every split (minimise the heights) |
| [ ] | 493 | [Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | H | Merge-sort counting |

## 10. Design with hashing

### About

These are design rounds built on hashing. The usual combination is a **map for lookups plus an array or list for indexing**. To delete from the list in O(1), swap the element with the last one and pop. To serialise a list of strings safely, prefix each one with its length.

### Example

Insert Delete GetRandom O(1), after inserting 5, 7 and 9: `vals = [5,7,9]` and `idx = {5:0, 7:1, 9:2}`. To remove 5, move the last value (9) into index 0, then pop. Now `vals = [9,7]` and `idx = {9:0, 7:1}`. `getRandom` picks a random index into `vals`.

### Template

```java
// Insert/Delete/GetRandom O(1): list of values + map from value to index
List<Integer> vals = new ArrayList<>();
Map<Integer, Integer> idx = new HashMap<>();
Random rnd = new Random();
boolean insert(int v) {
    if (idx.containsKey(v)) return false;
    idx.put(v, vals.size());
    vals.add(v);
    return true;
}
boolean remove(int v) {
    Integer i = idx.remove(v);
    if (i == null) return false;
    int last = vals.remove(vals.size() - 1);
    if (i < vals.size()) { vals.set(i, last); idx.put(last, i); }
    return true;
}
int getRandom() { return vals.get(rnd.nextInt(vals.size())); }

// Encode a list of strings with length prefixes: ["ab", "c#d"] -> "2#ab3#c#d"
StringBuilder sb = new StringBuilder();
for (String s : strs) sb.append(s.length()).append('#').append(s);
```

### Questions

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 706 | [Design HashMap](https://leetcode.com/problems/design-hashmap/) | E | Buckets + chaining |
| [ ] | 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) 🔒 | M | Length prefix |
| [ ] | 380 | [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | M | Map + list, swap with last ⭐ |

## Misc (mixed self-test)

These come up a lot in FAANG array rounds and mix the patterns above. Turn on **Hide patterns** and work out the technique yourself.

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 2352 | [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | M | Hash each row as a key |
| [ ] | 299 | [Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) | M | Digit counts |
| [ ] | 1497 | [Check If Array Pairs Are Divisible by k](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/) | M | Remainder counts |
| [ ] | 334 | [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | M | Track the two smallest so far |
| [ ] | 289 | [Game of Life](https://leetcode.com/problems/game-of-life/) | M | Encode old and new state in place |

## Covered in other topics

These are also on the array sections of Striver, Babbar or NeetCode, but they live with the technique they test:

- **Two Pointers ([02](02-Two-Pointers.md))**: Move Zeroes, Remove Duplicates from Sorted Array, Merge Sorted Array (Babbar's "merge without extra space"), 3Sum and 4Sum (Babbar's "triplet with given sum"), Trapping Rain Water, Two Sum II.
- **Sliding Window ([03](03-Sliding-Window.md))**: Best Time to Buy and Sell Stock, Minimum Size Subarray Sum (Babbar's "smallest subarray with sum greater than x"), Max Consecutive Ones III.
- **Binary Search ([05](05-Binary-Search.md))**: Search in Rotated Sorted Array, First and Last Position, Median of Two Sorted Arrays.
- **Linked List ([06](06-Linked-List.md))**: Find the Duplicate Number (Floyd's algorithm on the array).
- **Heaps ([09](09-Heaps.md))**: Kth Largest Element (Babbar's "Kth max and min").
- **DP 1D ([13](13-DP-1D.md))**: Maximum Product Subarray.
- **Greedy ([15](15-Greedy.md))**: Jump Game II (Babbar's "minimum jumps to reach the end").
- **Intervals ([16](16-Intervals.md))**: Merge Intervals.
- **Math & Geometry ([17](17-Math-and-Geometry.md))**: Set Matrix Zeroes, Rotate Image, Spiral Matrix.
- **Bit Manipulation ([18](18-Bit-Manipulation.md))**: Missing Number, Single Number.
- **Advanced ([19](19-Advanced-Optional.md))**: Count of Smaller Numbers After Self.

## GFG-only classics (no exact LeetCode version)

These appear on Striver's or Babbar's sheets. Each one uses a pattern from above, so you can do them on GeeksforGeeks once the matching subtopic feels comfortable:

- Second largest element (subtopic 1) · Union of two sorted arrays (two pointers) · Leaders in an array (subtopic 1, like 1299)
- Longest subarray with sum K, positives only (sliding window) · Largest subarray with 0 sum (subtopic 4, like 325 with k = 0) · Count subarrays with XOR = K (subtopic 4, with XOR instead of sum)
- Repeating and missing number (subtopic 7, like 645) · Count inversions (subtopic 9)
- Common elements in 3 sorted arrays (three pointers) · Array subset of another array (subtopic 2) · Factorial of a large number (digit array)
- Minimum swaps to bring elements ≤ K together (fixed sliding window) · Minimum merge operations to make an array a palindrome (two pointers)

## Pitfalls

- Prefix-sum map: forgetting to seed it with `pref.put(0, 1)` (for counting) or `first.put(0, -1)` (for longest).
- Using an `int[]` as a map key. Arrays hash by identity, so two equal arrays never match. Convert it to a `String` first.
- Comparing boxed `Integer`s with `==`. It only works for -128 to 127. Use `.equals()` or unbox to `int`.
- Adding to or removing from a collection inside a for-each loop over it, which throws `ConcurrentModificationException`.
- Negative numbers break the "shrink the window" approach. Use prefix sums instead.
- Java's `%` returns negative results for negative sums. Normalise with `((x % k) + k) % k`.
- Rotate by k: forgetting `k %= n` when k ≥ n.
- Dutch national flag: advancing `mid` after swapping with `hi`.

🔒 = requires LeetCode Premium (the same problem is free on NeetCode or LintCode). ⭐ = very frequently asked.

## My Notes

-
