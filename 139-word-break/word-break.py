class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True 
        for i in range(1, len(dp)):
            for word in wordDict:
                if s[i-len(word):i] == word:
                    dp[i] = dp[i] or dp[i-len(word)]
        return dp[-1]

        