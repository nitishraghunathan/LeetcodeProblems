class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        map_dict = {}
        for edge in edges:
            if edge[0] not in map_dict:
                map_dict[edge[0]] = []
            if edge[1] not in map_dict:
                map_dict[edge[1]] = []
            map_dict[edge[0]].append(edge[1])
            map_dict[edge[1]].append(edge[0])
        def dfs(map_dict: dict, src:int, destination:int, visited:set):
            if src == destination:
                return True
            visited.add(src)
            travels = map_dict[src]
            for travel in travels:
                if travel not in visited:
                    if dfs(map_dict, travel, destination, visited):
                        return True
            return False
        return dfs(map_dict, source, destination, set())
