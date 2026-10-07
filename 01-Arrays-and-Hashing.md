# 01 · Arrays & Hashing

> **Prereqs:** 00 · **Time:** 4–5 days

## When to use

- "Have I seen this before?", "count occurrences", "find the pair or complement": use a **hash map or set**.
- "Sum or count of a subarray": use **prefix sums**, often combined with a hash map.
- Grouping items by a property (anagrams, for example): use a **hash map with a canonical key**.
- Values in the range `1..n`: use **index as hash**, either cyclic sort or sign marking.

## Core concepts

- **Hash map**: average O(1) insert and lookup. Keys must be hashable, so use a `tuple` rather than a `list`.
- **Frequency counting**: `collections.Counter` or an array of 26 counts for lowercase letters.
- **Prefix sum**: `pre[i] = a[0] + ... + a[i-1]`, so `sum(a[l..r]) = pre[r+1] - pre[l]`.
- **Kadane's algorithm**: best subarray ending at i = `max(a[i], best_ending_at_{i-1} + a[i])`.
- **Bucket sort**: sorts in O(n) when the values are bounded (for example, by frequency ≤ n).

## Templates

```python
# Complement lookup (Two Sum)
seen = {}
for i, x in enumerate(nums):
    if target - x in seen:
        return [seen[target - x], i]
    seen[x] = i

# Prefix sum + hashmap: count subarrays with sum == k
count, cur = 0, 0
pref = {0: 1}
for x in nums:
    cur += x
    count += pref.get(cur - k, 0)
    pref[cur] = pref.get(cur, 0) + 1

# Kadane
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)

# Canonical key grouping
groups = defaultdict(list)
for w in words:
    key = tuple(sorted(w))   # or a 26-count tuple
    groups[key].append(w)
```

## Pitfalls

- Prefix-sum map: forgetting to seed it with `{0: 1}`.
- Using a list as a dictionary key. It must be a tuple.
- Mutating a list while iterating over it.
- Negative numbers break the "shrink the window" approach. Use prefix sums instead.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | E | Set |
| [ ] | 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | E | Counting |
| [ ] | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | E | Complement map |
| [ ] | 303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | E | Prefix sum |
| [ ] | 49 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | M | Canonical key |
| [ ] | 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | M | Bucket sort / heap |
| [ ] | 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | M | Prefix & suffix |
| [ ] | 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | M | Sets per row/col/box |
| [ ] | 271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) 🔒 | M | Length prefix |
| [ ] | 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | M | Set, start of sequence |
| [ ] | 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | M | Kadane |
| [ ] | 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | M | Prefix sum + map |
| [ ] | 75 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | M | Dutch national flag |
| [ ] | 41 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | H | Index as hash |

🔒 = requires LeetCode Premium (the same problem is free on NeetCode or LintCode).

## My Notes

-
