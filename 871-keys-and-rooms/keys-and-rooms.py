class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = []
        queue.append(0)
        visited = set()
        while queue:
            key = queue.pop(0)
            visited.add(key)
            for index, value in enumerate(rooms[key]):
                if value in visited:
                    continue
                queue.append(value)
        return len(rooms) == len(visited)
        