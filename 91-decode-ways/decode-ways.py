class Solution:
    def numDecodings(self, s: str) -> int:
        map_dict = {}
        for i in range(65, 91):
            map_dict[i-64] = chr(i)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] =0 if s[0] == '0' else 1
        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if int(s[i-2:i]) >= 10 and  int(s[i-2:i]) <=26:
                dp[i] +=dp[i-2]
        return dp[len(s)]

