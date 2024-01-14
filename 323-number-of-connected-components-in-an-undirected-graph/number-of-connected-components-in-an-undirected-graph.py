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
        RootX = self.find(x)
        RootY = self.find(y)
        if RootX != RootY:
            if self.rank[RootX] > self.rank[RootY]:
                self.root[RootY] = RootX
            elif self.rank[RootY] > self.rank[RootX]:
                self.root[RootX] = RootY
            else:
                self.root[RootX] = RootY
                self.rank[RootY] +=1
                            
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges = sorted(edges, key= lambda edges: edges[0])
        for edge in edges:
            uf.union(edge[0], edge[1])
        for i in range(n):
            uf.find(i)
        return len(set(uf.root))

