class Solution:
    def myPow(self, x: float, n: int) -> float:
        map_dict = {}
        def dfs(x, n):
            if n == 0:
                return 1
            if n in map_dict:
                return map_dict[n]
            power= None
            if n%2==1:
                power = dfs(x,n//2)*x*dfs(x,n//2)
            else:
                power = dfs(x,n//2)*dfs(x,n//2)
            map_dict[n] = power
            return map_dict[n]
        value= dfs(x,abs(n))
        if n < 0:
            return 1/value
        return value