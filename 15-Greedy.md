# 15 · Greedy

> **Prereqs:** 01, 09 · **Time:** 3 days

## When to use

- The choice that looks best right now **never needs to be undone**.
- Sorting by some key makes the next decision obvious.
- Reachability, or covering a range ("how far can I get?").
- If you can't prove the greedy choice is correct, the problem is probably DP.

## Core concepts

- **Exchange argument**: to prove greedy works, show that swapping any optimal solution's choice for the greedy choice doesn't make the result worse.
- **Track the furthest reachable point**: Jump Game I and II.
- **Running balance with a reset**: Gas Station (if the tank goes negative, restart from the next station).
- **Sort and process in order**: intervals, assigning cookies, hand of straights.
- **Two passes (left to right, then right to left)**: Candy, Trapping Rain Water.
- **Range of possibilities**: Valid Parenthesis String (track the minimum and maximum number of open brackets).

## Templates

```java
// Jump Game: reachability
int far = 0;
for (int i = 0; i < nums.length; i++) {
    if (i > far) return false;
    far = Math.max(far, i + nums[i]);
}
return true;

// Jump Game II: BFS-by-levels
int jumps = 0, end = 0, far = 0;
for (int i = 0; i < nums.length - 1; i++) {
    far = Math.max(far, i + nums[i]);
    if (i == end) {
        jumps++;
        end = far;
    }
}
return jumps;

// Gas Station
int total = 0, tank = 0, start = 0;
for (int i = 0; i < gas.length; i++) {
    total += gas[i] - cost[i];
    tank += gas[i] - cost[i];
    if (tank < 0) {
        tank = 0;
        start = i + 1;
    }
}
return total < 0 ? -1 : start;
```

## Pitfalls

- Using a greedy approach when the problem actually needs DP. Coin Change with arbitrary coin values is the classic trap.
- Sorting by the wrong key.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | E | Sort both lists |
| [ ] | 122 | [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | M | Sum the gains |
| [ ] | 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | M | Furthest reach |
| [ ] | 45 | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | M | BFS by levels |
| [ ] | 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | M | Running balance |
| [ ] | 846 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | M | Sort + counts |
| [ ] | 1899 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | M | Filter |
| [ ] | 763 | [Partition Labels](https://leetcode.com/problems/partition-labels/) | M | Last occurrence of each character |
| [ ] | 678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | M | Min/max open count |
| [ ] | 135 | [Candy](https://leetcode.com/problems/candy/) | H | Two passes |

## My Notes

-
