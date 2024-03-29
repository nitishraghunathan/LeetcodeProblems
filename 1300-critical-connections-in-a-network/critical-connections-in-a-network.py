class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = {}
        for i in range(n):
            if i not in graph:
                graph[i] = []
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        low = [n]*n
        critical_connections = []
        def dfs(src, discovery_time, parent):
            if low[src] == n:
                low[src] = discovery_time
                for i in graph[src]:
                    if i !=parent:
                        expected_time = discovery_time+1
                        actual_time = dfs(i, expected_time, src)
                        if actual_time >= expected_time:
                            critical_connections.append([src,i])
                        low[src] = min(low[src], low[i])
            return low[src]
        dfs(n-1,0,-1)
        return critical_connections