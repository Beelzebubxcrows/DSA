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

```java
// Reverse
ListNode prev = null, cur = head;
while (cur != null) {
    ListNode nxt = cur.next;
    cur.next = prev;
    prev = cur;
    cur = nxt;
}
return prev;

// Middle (returns second middle for even length)
ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
}

// Cycle start (Floyd)
ListNode slow = head, fast = head;
while (fast != null && fast.next != null) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow == fast) {
        ListNode p = head;
        while (p != slow) {
            p = p.next;
            slow = slow.next;
        }
        return p;
    }
}
return null;

// Dummy node merge
ListNode dummy = new ListNode(), tail = dummy;
while (a != null && b != null) {
    if (a.val <= b.val) { tail.next = a; a = a.next; }
    else { tail.next = b; b = b.next; }
    tail = tail.next;
}
tail.next = (a != null) ? a : b;
return dummy.next;
```

## Pitfalls

- Losing the reference to `next` before you rewire the pointers.
- Not checking `fast != null && fast.next != null`, which throws a `NullPointerException`.
- Forgetting to cut the list (`mid.next = null`) when splitting it.
- `==` on nodes compares references, which is what you want for "same node". Compare values with `.val`.

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
