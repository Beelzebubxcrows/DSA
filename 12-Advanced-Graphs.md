# 12 · Advanced Graphs

> **Prereqs:** 09, 11 · **Time:** 4 days

## When to use

- **Weighted** shortest path with non-negative weights: **Dijkstra**.
- Shortest path with a limit on the number of edges, or with negative weights: **Bellman-Ford**.
- Shortest paths between every pair of nodes, with small n: **Floyd–Warshall**, which is O(n³).
- Connecting every node at the lowest total cost: **minimum spanning tree** (Prim's or Kruskal's algorithm).
- Minimising the maximum edge along a path: a modified Dijkstra, or binary search combined with BFS.
- Using every edge exactly once: an **Eulerian path** (Hierholzer's algorithm).
- Critical edges or articulation points: **Tarjan's algorithm**.

## Core concepts

- **Dijkstra**: uses a min-heap of `(dist, node)`. When you pop an entry whose distance is out of date, skip it. Runs in O(E log V).
- **Kruskal**: sort the edges by weight, then add each edge with Union-Find if it doesn't create a cycle. Runs in O(E log E).
- **Prim**: grow the tree from one node, using a min-heap of the edges that cross out of the tree.
- **Bellman-Ford**: relax every edge V−1 times. For "at most K stops", run K+1 rounds and copy the distance array each round.

## Templates

```python
# Dijkstra
dist = {src: 0}
h = [(0, src)]
while h:
    d, u = heapq.heappop(h)
    if d > dist.get(u, float('inf')): continue   # stale
    for v, w in adj[u]:
        nd = d + w
        if nd < dist.get(v, float('inf')):
            dist[v] = nd
            heapq.heappush(h, (nd, v))

# Kruskal (with Union-Find from topic 11)
edges.sort(key=lambda e: e[2])
cost = 0
for u, v, w in edges:
    if union(u, v): cost += w

# Bellman-Ford with at most K edges
dist = [inf] * n; dist[src] = 0
for _ in range(K + 1):
    tmp = dist[:]
    for u, v, w in flights:
        if dist[u] + w < tmp[v]: tmp[v] = dist[u] + w
    dist = tmp
```

## Pitfalls

- Dijkstra gives wrong answers with negative edge weights.
- Bellman-Ford with a stop limit: not copying the distance array each round lets a path use more edges than allowed in one round.
- Forgetting to skip out-of-date heap entries, which makes the algorithm much slower.

## Problems

| ✓ | # | Problem | Diff | Pattern |
|---|---|---------|------|---------|
| [ ] | 743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | M | Dijkstra ⭐ |
| [ ] | 1514 | [Path with Maximum Probability](https://leetcode.com/problems/path-with-maximum-probability/) | M | Dijkstra with a max-heap |
| [ ] | 1631 | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | M | Minimax Dijkstra |
| [ ] | 1584 | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | M | Prim / Kruskal |
| [ ] | 787 | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | M | Bellman-Ford |
| [ ] | 721 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | M | Union-Find |
| [ ] | 778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/) | H | Minimax Dijkstra |
| [ ] | 332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | H | Eulerian path |
| [ ] | 269 | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) 🔒 | H | Build graph + topological sort ⭐ |
| [ ] | 1192 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | H | Tarjan bridges |

## My Notes

-
