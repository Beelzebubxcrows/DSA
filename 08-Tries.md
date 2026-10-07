# 08 · Tries

> **Prereqs:** 07 · **Time:** 1–2 days

## When to use

- **Prefix** queries: autocomplete, "starts with", or replacing words with their roots.
- Searching for many words in a grid at once (Word Search II).
- Wildcard matching against a dictionary.
- **Bitwise trie**: maximising XOR between pairs of numbers.

## Core concepts

- Each node holds `children: dict[char, Node]` and an `end` flag (or stores the word itself).
- Insert and search take O(L) time, where L is the word length. Space is O(total number of characters).
- To handle wildcards such as `.`, run a DFS over every child at that position.

## Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.end = True

    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node.children: return None
            node = node.children[c]
        return node

    def search(self, word):
        n = self._walk(word); return bool(n and n.end)

    def startsWith(self, prefix):
        return self._walk(prefix) is not None
```

## Pitfalls

- Word Search II: you need to **prune** found words from the trie, or the solution exceeds the time limit.
- Forgetting the `end` flag, which makes `search("app")` return True when only "apple" was inserted.

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
