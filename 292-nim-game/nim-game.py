class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        Trying to make sure your opponent always gives you a turn to canWinNim
        """
        return n%4 !=0
