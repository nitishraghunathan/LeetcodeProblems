class Solution:
    def countSegments(self, s: str) -> int:
        left, right = 0, len(s)
        counter = 0
        flag = False
        while left < right:
            while left < right and s[left] == " ":
                left+=1
            while left < right and s[left]!= " ":
                left += 1
                flag = True
            if flag:
                counter+=1
                flag = False
        return counter
        
