class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if s[i-len(word):i] == word:
                    if not dp[i]:
                        dp[i] = dp[i-len(word)]
        print(dp)
        return dp[-1]