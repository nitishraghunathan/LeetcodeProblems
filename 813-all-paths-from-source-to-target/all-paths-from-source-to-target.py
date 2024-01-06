class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        def dfs(graph: list, src:int, result:list, path: list, visited: set):
            if src == len(graph)-1:
                path.append(src)
                result.append(list(path))
                path.pop()
                return result
            visited.add(src)
            path.append(src)
            for tree in graph[src]:
                if tree not in visited:
                    result = dfs(graph, tree, result, path, visited)
            if path:
                visited.remove(path.pop())
            return result
        return dfs(graph, 0, [], [], set())