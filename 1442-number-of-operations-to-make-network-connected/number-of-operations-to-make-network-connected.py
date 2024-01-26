class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n
        self.extra = 0
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rooty != rootx:
            if self.rank[rootx] >= self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
            else: 
                self.root[rooty] = rootx
                self.rank[rootx] +=1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        uf = UnionFind(n)
        for connection in connections:
            if not uf.is_connected(connection[0], connection[1]):
                uf.union(connection[0], connection[1])
                n-=1
        return n-1