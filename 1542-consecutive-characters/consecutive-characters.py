class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        low = 0
        max_value = 1
        temp = s[0]
        for index, value in enumerate(s):
            if temp !=value:
                max_value = max(index-low, max_value)
                low = index
                temp=value
        return max(index+1-low, max_value)


