class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Algorithm: check if the first digit is zero
        if no then add dp[1] = 1
        dp[0] = 1 always as there will always be 1 way to represent an empty string 
        dp[1] = 1 if s[i-1]!='0'
        no starting from 2nd index lets say how many ways can  be formed. 
        s[i-1] is not zero then there would be atleast dp[i-1] ways 
        else if s[i-2:i] <26 and >10 then +dp[i-2] ways 
        """
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] =0 if s[0] == '0' else 1
        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if int(s[i-2:i]) >= 10 and  int(s[i-2:i]) <=26:
                dp[i] +=dp[i-2]
        return dp[len(s)]



