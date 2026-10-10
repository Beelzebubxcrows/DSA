# 08 · Tries

> **Prereqs:** 07 · **Time:** 1–2 days

## When to use

- **Prefix** queries: autocomplete, "starts with", or replacing words with their roots.
- Searching for many words in a grid at once (Word Search II).
- Wildcard matching against a dictionary.
- **Bitwise trie**: maximising XOR between pairs of numbers.

## Core concepts

- Each node holds `Node[] children = new Node[26]` for lowercase letters (or a `Map<Character, Node>` for a larger alphabet) and an `end` flag (or stores the word itself).
- Insert and search take O(L) time, where L is the word length. Space is O(total number of characters).
- To handle wildcards such as `.`, run a DFS over every child at that position.

## Template

```java
// Trie (lowercase letters)
class Trie {
    private static class Node {
        Node[] children = new Node[26];
        boolean end;
    }
    private final Node root = new Node();

    public void insert(String word) {
        Node node = root;
        for (char c : word.toCharArray()) {
            int i = c - 'a';
            if (node.children[i] == null) node.children[i] = new Node();
            node = node.children[i];
        }
        node.end = true;
    }

    private Node walk(String s) {
        Node node = root;
        for (char c : s.toCharArray()) {
            node = node.children[c - 'a'];
            if (node == null) return null;
        }
        return node;
    }

    public boolean search(String word) {
        Node n = walk(word);
        return n != null && n.end;
    }

    public boolean startsWith(String prefix) {
        return walk(prefix) != null;
    }
}
```

## Pitfalls

- Word Search II: you need to **prune** found words from the trie, or the solution exceeds the time limit.
- Forgetting the `end` flag, which makes `search("app")` return true when only "apple" was inserted.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | E | Warm-up (no trie needed) |
| [ ] | 208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | M | Core |
| [ ] | 211 | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | M | Wildcard DFS |
| [ ] | 648 | [Replace Words](https://leetcode.com/problems/replace-words/) | M | Shortest prefix |
| [ ] | 1268 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | M | Prefix + sorting |
| [ ] | 421 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | M | Bitwise trie |
| [ ] | 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | H | Trie + grid DFS ⭐ |

## My Notes

-
