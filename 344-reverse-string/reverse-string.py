class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        1. we use two pointers start and end
        2. swap start position with end position characters
        3. return the string
        """
        start = 0
        end = len(s) -1 
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s
        