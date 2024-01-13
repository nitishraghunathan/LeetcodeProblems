# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    class UnionFind:
        def __init__(self, n):
            self.root = [i for i in range(n)]
        def find(x):
            if x == root[x]:
                return x
            root[x] = self.find(root[x])
            return root[x]
        
        def union(x, y):
            RootX = self.find(x)
            RootY = self.find(y)
            if RootX != RootY:
                self.root[RootX] = RootY
        
        def is_connected(x,y):
            return self.root[x] == self.root[y]
             
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        root = [i for i in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if root[i] != root[j]:
                    if categoryHandler.haveSameCategory(i,j):
                        root[j] = i
        return len(set(root))
           