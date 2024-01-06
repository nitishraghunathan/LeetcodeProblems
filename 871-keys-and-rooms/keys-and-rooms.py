class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(rooms:list, src:int, visited: set):
            visited.add(src)
            if len(visited) == len(rooms):
                return True
            flag = False
            for dest in rooms[src]:
                if dest not in visited:
                    flag |= dfs(rooms, dest, visited)
            return flag
        return dfs(rooms,0, set())