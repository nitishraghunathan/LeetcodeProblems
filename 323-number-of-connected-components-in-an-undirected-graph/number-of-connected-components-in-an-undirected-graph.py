class UnionFind:
    def __init__(self, n):
        self.rank = [1 for i in range(n)]
        self.root = [i for i in range(n)]
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x!=root_y:
            if self.rank[root_x] >= self.rank[root_y]:
                self.root[root_y] = root_x
                self.rank[root_x] +=1
            else:
                self.root[root_x] = root_y
                self.rank[root_y] +=1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n) 
        edges = sorted(edges, key=lambda x:x[0])
        for edge in edges:
            uf.union(edge[0], edge[1])
        for i in range(n):
            uf.find(i)
        return len(set(uf.root))