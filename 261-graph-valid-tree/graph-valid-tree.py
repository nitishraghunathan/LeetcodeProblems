class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph_dict = {}
        if len(edges) != n-1:
            return False
        for i in range(n):
            if i not in graph_dict:
                graph_dict[i] = []
        for edge in edges:
            graph_dict[edge[0]].append(edge[1])
            graph_dict[edge[1]].append(edge[0])
        visited = set()
        def dfs(graph_dict: dict, node: int):
            if node in visited:
                return
            visited.add(node)
            for value in graph_dict[node]:
                result = dfs(graph_dict, value)
            return
        dfs(graph_dict, 0)
        return len(visited) == n
        