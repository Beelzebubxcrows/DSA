# 03 · Sliding Window

> **Prereqs:** 01, 02 · **Time:** 3–4 days

## When to use

- The problem asks for the longest, shortest or count of **contiguous** subarrays or substrings that satisfy a condition.
- The condition is **monotonic**: if a window is valid, so are its sub-windows (or it only becomes invalid as it grows).
- A window of fixed size k.

## Core concepts

- **Fixed window**: add `a[r]`, remove `a[r-k]`.
- **Variable window**: expand `r` every step and shrink `l` while the window is invalid.
- Keep the window's state up to date incrementally with a counter, sum or set.
- **"Exactly K" = atMost(K) − atMost(K−1).**
- Sliding window maximum: use a **monotonic deque**.
- ⚠️ Sliding window doesn't work with **negative numbers** for sum conditions. Use prefix sums instead.

## Templates

```python
# Variable window: longest valid
l = 0
state = defaultdict(int)
best = 0
for r, x in enumerate(s):
    state[x] += 1
    while not valid(state):
        state[s[l]] -= 1
        l += 1
    best = max(best, r - l + 1)

# Variable window: shortest valid
l, best = 0, float('inf')
for r in range(len(a)):
    add(a[r])
    while valid():
        best = min(best, r - l + 1)
        remove(a[l]); l += 1

# Monotonic deque for window max
dq = deque()  # indices, values decreasing
for i, x in enumerate(nums):
    while dq and nums[dq[-1]] <= x: dq.pop()
    dq.append(i)
    if dq[0] <= i - k: dq.popleft()
    if i >= k - 1: res.append(nums[dq[0]])
```

## Pitfalls

- Updating the answer at the wrong point. For "longest", update after shrinking. For "shortest", update while shrinking.
- Forgetting to delete counter keys that reach 0 when you rely on `len(state)`.
- Off-by-one errors in the window length `r - l + 1`.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | E | Track the minimum so far |
| [ ] | 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | M | Variable, set |
| [ ] | 424 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | M | len − maxfreq ≤ k |
| [ ] | 567 | [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | M | Fixed, counts |
| [ ] | 438 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | M | Fixed, counts |
| [ ] | 209 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | M | Shortest valid |
| [ ] | 1004 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | M | At most k zeros |
| [ ] | 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | H | Shortest valid, "have" vs "need" counts |
| [ ] | 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | H | Monotonic deque |
| [ ] | 992 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | H | atMost(K) − atMost(K−1) |

## My Notes

-
