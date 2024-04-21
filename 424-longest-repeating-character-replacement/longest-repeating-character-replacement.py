class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Two pointer mechanism
        ABAB
        ABAB
        ACAB  

        AAABABBA
        index = 0 
        counter +1      
        """
        count = {}
        max_frequency = float('-inf')
        result = 0
        left = 0
        for index, char in enumerate(s):
            count[char] = count.get(char,0)+1
            max_frequency = max(max_frequency, count[char])
            while index - left +1 - max_frequency > k:
                count[s[left]]-=1
                left+=1
            result = max(result, index-left+1)
        return result
                
                
