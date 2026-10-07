# 11 · Graphs

> **Prereqs:** 07, 10 · **Time:** 5–6 days

## When to use

- Grids (islands, flood fill), networks, dependencies, states connected by transitions.
- "Number of connected components", "can you reach X", or "shortest path with unweighted edges" (use BFS).
- Prerequisites or ordering: **topological sort**.
- Dynamic connectivity, or detecting a cycle in an undirected graph: **Union-Find**.

## Core concepts

- **Representations**: an adjacency list (`defaultdict(list)`), or an implicit grid where each cell's neighbours are found with direction vectors.
- **DFS** is good for reachability, components, cycle detection and flood fill.
- **BFS** gives the **shortest path in an unweighted graph**. **Multi-source BFS** starts with every source in the queue (rotting oranges, walls and gates).
- **Topological sort (Kahn's algorithm)**: start the BFS from nodes with in-degree 0. If you process fewer than n nodes, the graph has a cycle.
- **Cycle detection in a directed graph**: DFS with three colours (unvisited, visiting, visited).
- **Union-Find**: path compression plus union by rank gives about O(α(n)) per operation.
- **Bipartite check**: two-colour the graph with BFS or DFS.
- **Reverse thinking**: start from the boundary or the target instead (Pacific Atlantic, Surrounded Regions).
- Complexity is O(V + E). For a grid, that's O(R·C).

## Templates

```python
DIRS = ((1,0),(-1,0),(0,1),(0,-1))

# Grid DFS (flood fill)
def dfs(r, c):
    if not (0 <= r < R and 0 <= c < C) or grid[r][c] != '1': return
    grid[r][c] = '0'
    for dr, dc in DIRS: dfs(r+dr, c+dc)

# BFS shortest path (unweighted)
q = deque([(start, 0)]); seen = {start}
while q:
    node, d = q.popleft()
    if node == target: return d
    for nb in adj[node]:
        if nb not in seen:
            seen.add(nb); q.append((nb, d + 1))

# Topological sort (Kahn)
indeg = [0] * n
for u, v in edges: adj[u].append(v); indeg[v] += 1
q = deque(i for i in range(n) if indeg[i] == 0)
order = []
while q:
    u = q.popleft(); order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
has_cycle = len(order) < n

# Union-Find
parent = list(range(n)); rank = [0] * n
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: return False
    if rank[ra] < rank[rb]: ra, rb = rb, ra
    parent[rb] = ra
    if rank[ra] == rank[rb]: rank[ra] += 1
    return True
```

## Pitfalls

- Marking a node visited when you **pop** it in BFS instead of when you **push** it, which leads to duplicate work.
- Getting the direction of prerequisite edges backwards.
- Recursion depth on large grids. Mention that an iterative BFS avoids it.
- Forgetting isolated nodes (nodes with no edges).

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | M | Grid DFS ⭐ |
| [ ] | 695 | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | M | Grid DFS |
| [ ] | 133 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | M | DFS + map from old node to new |
| [ ] | 994 | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | M | Multi-source BFS ⭐ |
| [ ] | 286 | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) 🔒 | M | Multi-source BFS |
| [ ] | 417 | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | M | Reverse from the borders |
| [ ] | 130 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | M | Reverse from the borders |
| [ ] | 547 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | M | DFS / Union-Find |
| [ ] | 323 | [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) 🔒 | M | Union-Find |
| [ ] | 261 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) 🔒 | M | n−1 edges + connected |
| [ ] | 785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | M | Two-colouring |
| [ ] | 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | M | Topological sort / cycle ⭐ |
| [ ] | 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | M | Topological order |
| [ ] | 684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | M | Union-Find |
| [ ] | 1091 | [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | M | BFS on a grid |
| [ ] | 127 | [Word Ladder](https://leetcode.com/problems/word-ladder/) | H | BFS over word states |

## My Notes

-
