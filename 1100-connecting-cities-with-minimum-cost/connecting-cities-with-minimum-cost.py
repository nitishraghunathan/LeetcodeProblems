class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        result = []
      
        map_dict = {}
        visited = set()
        for connection in connections:
            if connection[0] not in map_dict:
                map_dict[connection[0]] = []
            if connection[1] not in map_dict:
                map_dict[connection[1]] = []
            map_dict[connection[0]].append([connection[2], connection[1]])
            map_dict[connection[1]].append([connection[2], connection[0]])

        total_cost = 0
        for key in map_dict[1]:
            heapq.heappush(result, key)
        heapq.heapify(result)
        visited.add(1)
        while result:
            array = heapq.heappop(result)
            if array[1] not in visited:
                visited.add(array[1])
                total_cost += array[0]
                for key in map_dict[array[1]]:
                    heapq.heappush(result, key)

        return total_cost if len(visited) == n else -1