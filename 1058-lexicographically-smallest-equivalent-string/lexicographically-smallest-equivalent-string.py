"""
we need to find potential ways.

1. a graph can be modelled for this problem 
Brute force -> compare each character and find the smallest mapping.
We can use union Find.
Time complexity -> O(N) for find 
O(N) -> for union 
"""
class UnionFind:
    def __init__(self):
        self.root = [i for i in range(26)]
        self.rank = [26-i for i in range(26)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] >= self.rank[rooty]:
                for index,value in enumerate(self.root):
                    if value == rooty:
                        self.root[index] = self.root[rootx]
            else:
                for index,value in enumerate(self.root):
                    if value == rootx:
                        self.root[index] = self.root[rooty]
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for one, two in zip(s1, s2):
            uf.union(ord(one)-97, ord(two) -97)
        new_str = ''
        for characters in baseStr:
            new_str += chr(uf.root[ord(characters)-97] + 97)
        return new_str