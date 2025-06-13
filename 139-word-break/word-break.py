class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_dict = set(wordDict)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(len(s)+1):
            for word in word_dict:
                size = len(word)
                if i >=size and s[i-size:i] == word:
                    dp[i] = dp[i-size] or dp[i]
        return dp[-1]


        