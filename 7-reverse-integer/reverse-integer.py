class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        signed = False if x > 0 else True
        x = x if x> 0 else -x
        new_str = ""
        while x > 0:
            new_str += str(x%10)
            x//=10
        new_int = int(new_str)
        if signed:
            new_int = -new_int
        return new_int if -2**31 < new_int < 2**31 - 1 else 0