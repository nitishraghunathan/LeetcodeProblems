class UnionFind:
    def __init__(self, x):
        self.root = [i for i in range(x)]
        self.rank = [1]*x
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rooty != rootx:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = self.root[rootx]
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = self.root[rooty]
            else:
                self.root[rooty] =self.root[rootx]
                self.rank[rootx] += 1
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.is_connected(edge[0]-1, edge[1]-1):
                uf.union(edge[0]-1, edge[1]-1)
            else:
                return edge
        return []