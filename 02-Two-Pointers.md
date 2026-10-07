# 02 · Two Pointers

> **Prereqs:** 01 · **Time:** 2–3 days

## When to use

- The input is **sorted**, or sorting it doesn't break the problem, and you're looking for a pair or triplet with a target sum.
- Palindrome checks, or comparing from both ends.
- **In-place** array changes such as removing elements, deduplicating or partitioning.
- Merging two sorted sequences.

## Core concepts

- **Opposite ends**: `l = 0, r = n - 1`, then move the pointers inward based on a comparison.
- **Same direction (fast/slow, read/write)**: one pointer reads every element and the other marks where the next valid element is written.
- **Reducing k-Sum**: sort, fix one element, then run two-sum on the rest. 3Sum is O(n²) and 4Sum is O(n³).

## Templates

```python
# Opposite ends on a sorted array
l, r = 0, len(a) - 1
while l < r:
    s = a[l] + a[r]
    if s == target: return [l, r]
    if s < target: l += 1
    else: r -= 1

# Read/write pointer (in-place filter)
w = 0
for x in nums:
    if keep(x):
        nums[w] = x
        w += 1
return w

# 3Sum skeleton with duplicate skipping
nums.sort()
for i in range(len(nums)):
    if i and nums[i] == nums[i-1]: continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0: l += 1
        elif s > 0: r -= 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]: l += 1
```

## Pitfalls

- Not skipping duplicates in 3Sum or 4Sum.
- Using `l <= r` when the two pointers must point at different elements.
- Sorting when you need to return the original indices.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | E | Opposite ends |
| [ ] | 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | E | Read/write |
| [ ] | 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | E | Read/write |
| [ ] | 88 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | E | Fill from the back |
| [ ] | 167 | [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | M | Opposite ends |
| [ ] | 15 | [3Sum](https://leetcode.com/problems/3sum/) | M | Sort + fix + 2ptr |
| [ ] | 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | M | Move the shorter side |
| [ ] | 18 | [4Sum](https://leetcode.com/problems/4sum/) | M | k-Sum reduction |
| [ ] | 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | H | Left/right max |

## My Notes

-
