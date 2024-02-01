from collections import defaultdict
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        visited = set()
        m,n = len(grid), len(grid[0])
        id = defaultdict(lambda:-1)
        value = defaultdict(int)
        def dfs(v, idx):
            if v in visited: return 0
            visited.add(v)
            id[v] = idx
            i,j = v
            res = grid[i][j]
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj] != -1:
                    res += dfs((i+di,j+dj), idx)
            return res 
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1 and (i,j) not in visited:
                    cur = dfs((i,j), idx)
                    value[idx] = cur 
                    idx += 1
        total = sum(value.values())
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    res += total - value[id[(i,j)]]
        return res

        

        