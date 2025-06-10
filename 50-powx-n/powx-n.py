class Solution:
    def myPow(self, x: float, n: int) -> float:
        map_dict = {}
        if n < 0:
            x = 1/x
            n = -n
        map_dict[0] = 1
        def recursion(x: float, n:int):
            if n == 0:
                return 1
            if n in map_dict:
                return map_dict[n]
            compute_x_power = recursion(x, n//2)*recursion(x, n//2)
            if n%2 == 0:
                map_dict[n] = compute_x_power
            else:
                map_dict[n] = compute_x_power*x
            return map_dict[n]
        recursion(x,n)
        return map_dict[n]
        