# 06 · Linked List

> **Prereqs:** 02 · **Time:** 3 days

## When to use

- The input is a linked list, or you're designing structures like an LRU cache (hash map plus doubly linked list).
- Cycle detection, including "find the duplicate" problems on arrays treated as a linked list.

## Core concepts

- **Dummy (sentinel) node**: makes it easier to handle changes to the head.
- **Fast/slow pointers (Floyd's algorithm)**: finds the middle of the list, detects cycles, and locates the start of a cycle.
- **In-place reversal**: uses three pointers, `prev`, `cur` and `nxt`.
- **The gap technique**: to remove the nth node from the end, move `fast` n steps ahead first.
- Many problems are combinations of three steps: find the middle, reverse the second half, then merge.

## Templates

```python
# Reverse
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
return prev

# Middle (returns second middle for even length)
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next

# Cycle start (Floyd)
slow = fast = head
while fast and fast.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
        p = head
        while p is not slow:
            p, slow = p.next, slow.next
        return p
return None

# Dummy node merge
dummy = tail = ListNode()
while a and b:
    if a.val <= b.val: tail.next, a = a, a.next
    else: tail.next, b = b, b.next
    tail = tail.next
tail.next = a or b
return dummy.next
```

## Pitfalls

- Losing the reference to `next` before you rewire the pointers.
- Not checking `fast and fast.next`.
- Forgetting to cut the list (`mid.next = None`) when splitting it.
- Use `is` to compare nodes, not `==`.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | E | Reversal |
| [ ] | 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | E | Dummy node |
| [ ] | 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | E | Fast/slow |
| [ ] | 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | E | Fast/slow |
| [ ] | 19 | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | M | Gap |
| [ ] | 143 | [Reorder List](https://leetcode.com/problems/reorder-list/) | M | Middle + reverse + merge |
| [ ] | 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | M | Carry |
| [ ] | 138 | [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | M | Hash map / interleave |
| [ ] | 142 | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | M | Floyd cycle start |
| [ ] | 287 | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) | M | Array as a linked list |
| [ ] | 146 | [LRU Cache](https://leetcode.com/problems/lru-cache/) | M | Hash map + doubly linked list ⭐ |
| [ ] | 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | H | Heap / divide and conquer |
| [ ] | 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | H | Reverse in chunks |

⭐ = very frequently asked

## My Notes

-
