class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        left, right = 0, len(bits)-1
        while left <= right:
            if left == right:
                return True
            if bits[left] == 1:
                left +=2
            else:
                left+=1
        return False
        