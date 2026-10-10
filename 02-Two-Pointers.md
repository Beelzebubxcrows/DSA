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

```java
// Opposite ends on a sorted array
int l = 0, r = a.length - 1;
while (l < r) {
    int s = a[l] + a[r];
    if (s == target) return new int[]{l, r};
    if (s < target) l++;
    else r--;
}

// Read/write pointer (in-place filter)
int w = 0;
for (int x : nums)
    if (keep(x)) nums[w++] = x;
return w;

// 3Sum skeleton with duplicate skipping
Arrays.sort(nums);
List<List<Integer>> res = new ArrayList<>();
for (int i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] == nums[i - 1]) continue;
    int l = i + 1, r = nums.length - 1;
    while (l < r) {
        int s = nums[i] + nums[l] + nums[r];
        if (s < 0) l++;
        else if (s > 0) r--;
        else {
            res.add(List.of(nums[i], nums[l], nums[r]));
            l++;
            while (l < r && nums[l] == nums[l - 1]) l++;
        }
    }
}
```

## Pitfalls

- Not skipping duplicates in 3Sum or 4Sum.
- 4Sum: adding four `int`s can overflow. Compute the sum as a `long`.
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
