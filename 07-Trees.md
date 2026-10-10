# 07 · Trees

> **Prereqs:** recursion basics · **Time:** 5–6 days (this topic comes up a lot)

## When to use

- The input is a binary tree or BST, a hierarchy, or a parsed structure.
- Questions about depth, diameter, paths, ancestors, level-by-level views, or serialization.

## Core concepts

- **DFS orders**: pre-order (node, left, right), in-order (left, node, right; **gives sorted order for a BST**), and post-order (left, right, node; use it when a parent needs results from its children).
- **BFS / level order**: uses a queue and processes the tree one level at a time.
- **BST property**: every value in the left subtree is less than the node, which is less than every value in the right subtree. Validate with **min and max bounds**, not by comparing each node only with its children.
- **The "return one thing, update a global" pattern**: used for diameter and maximum path sum. The recursive call returns the best single branch, and a global variable tracks the best path that passes through the current node.
- Height is O(log n) if the tree is balanced and O(n) if it's skewed. That height is the recursion stack space.

## Templates

```java
// DFS returning a value (height)
int height(TreeNode node) {
    if (node == null) return 0;
    return 1 + Math.max(height(node.left), height(node.right));
}

// Return-one, update-global (diameter)
int best = 0;   // a field, so the recursive method can update it
int dfs(TreeNode node) {
    if (node == null) return 0;
    int L = dfs(node.left), R = dfs(node.right);
    best = Math.max(best, L + R);
    return 1 + Math.max(L, R);
}

// BFS level order
List<List<Integer>> res = new ArrayList<>();
Queue<TreeNode> q = new ArrayDeque<>();
if (root != null) q.offer(root);
while (!q.isEmpty()) {
    List<Integer> level = new ArrayList<>();
    for (int size = q.size(); size > 0; size--) {
        TreeNode node = q.poll();
        level.add(node.val);
        if (node.left != null) q.offer(node.left);
        if (node.right != null) q.offer(node.right);
    }
    res.add(level);
}

// Validate BST with bounds (long, so nodes equal to Integer.MIN/MAX_VALUE still pass)
boolean valid(TreeNode node, long lo, long hi) {
    if (node == null) return true;
    if (node.val <= lo || node.val >= hi) return false;
    return valid(node.left, lo, node.val) && valid(node.right, node.val, hi);
}
// call: valid(root, Long.MIN_VALUE, Long.MAX_VALUE)

// Iterative inorder
Deque<TreeNode> st = new ArrayDeque<>();
TreeNode cur = root;
while (!st.isEmpty() || cur != null) {
    while (cur != null) {
        st.push(cur);
        cur = cur.left;
    }
    cur = st.pop();
    visit(cur);
    cur = cur.right;
}
```

## Pitfalls

- Validating a BST by comparing each node only with its direct children.
- BST bounds as `int`: a node holding `Integer.MAX_VALUE` fails a `< Integer.MAX_VALUE` check. Use `long` bounds or nullable `Integer` bounds.
- BFS: writing `for (int i = 0; i < q.size(); i++)` while adding children. `q.size()` changes inside the loop, so read it once first.
- Handling `null` children inconsistently.
- Max path sum: forgetting to clamp negative branches to 0.
- Java's default stack allows a recursion depth of roughly 10⁴, so a skewed tree with 10⁵ nodes can throw `StackOverflowError`. Mention this in the interview and offer the iterative version.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | E | DFS |
| [ ] | 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | E | DFS |
| [ ] | 100 | [Same Tree](https://leetcode.com/problems/same-tree/) | E | DFS on two trees |
| [ ] | 572 | [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | E | Same Tree at every node |
| [ ] | 110 | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | E | Height + flag |
| [ ] | 543 | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | E | Return-one, update-global |
| [ ] | 102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | M | BFS |
| [ ] | 199 | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | M | BFS, last node per level |
| [ ] | 1448 | [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | M | Pass the max down |
| [ ] | 98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | M | Bounds |
| [ ] | 230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | M | In-order |
| [ ] | 235 | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | M | Use the BST property |
| [ ] | 236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | M | Post-order ⭐ |
| [ ] | 105 | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | M | Index map |
| [ ] | 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | H | Return-one, update-global ⭐ |
| [ ] | 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | H | Pre-order with null markers |

## My Notes

-
