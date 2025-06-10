class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        edges = sorted(edges)
        for edge in edges:
            uf.union(edge[0], edge[1])
        for i in range(n):
            uf.find(i)
        return len(set(uf.root))
        



class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if self.rank[rootx] >= self.rank[rooty]:
            self.root[rooty] = rootx
            self.rank[rootx] +=1
        else:
            self.root[rootx] = rooty
            self.rank[rooty] +=1
        