class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        low = 0
        high = len(number) -1
        while low < high:
            if number[low] != number[high]:
                return False
            low+=1
            high -=1
        return True