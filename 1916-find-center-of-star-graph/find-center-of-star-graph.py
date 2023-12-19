class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        map_dict = {}
        for edge in edges:
            if edge[0] not in map_dict:
                map_dict[edge[0]] = []
            if edge[1] not in map_dict:
                map_dict[edge[1]] = []

            map_dict[edge[0]].append(edge[1])
            map_dict[edge[1]].append(edge[0])
        max_count = 0
        index = -1
        for key,value in map_dict.items():
            if len(value) > max_count:
                max_count = len(value)
                index = key
        return index
