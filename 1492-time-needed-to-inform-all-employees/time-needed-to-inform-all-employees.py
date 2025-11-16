class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        max_count = [0]
        def dfs(source: int, visited: set, count:int):
            nonlocal max_count
            visited.add(source)
            for children in map_dict[source]:
                if children[0] not in visited:
                    dfs(children[0], visited, count+children[1])
            max_count[0] = max(max_count[0], count)
            return
        map_dict = {}
        for i in range(n):
            if i not in map_dict:
                map_dict[i] =[]
        for index, manager in enumerate(managers):
            if manager ==-1:
                continue
            map_dict[manager].append([index, informTime[index]])
        dfs(headID, set(), informTime[headID])
        return max_count[0]

        