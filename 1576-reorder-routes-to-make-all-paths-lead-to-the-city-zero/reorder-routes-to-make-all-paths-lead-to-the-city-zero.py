class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Build undirected graph
        graph = [[] for _ in range(n)]
        
        for u, v in connections:
            graph[u].append((v, 1))  # original direction
            graph[v].append((u, 0))  # reverse direction
        
        queue = deque([0])
        visited = set([0])
        changes = 0
        
        while queue:
            node = queue.popleft()
            for neighbor, is_forward in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if is_forward == 1:
                        changes += 1
                    queue.append(neighbor)
        
        return changes