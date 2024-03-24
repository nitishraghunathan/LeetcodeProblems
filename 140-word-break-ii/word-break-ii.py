class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # dp = [False]*(len(s)+1)
        # dp[0] = True
        # for i in range(1, len(dp)):
        #     for j in range(len(wordDict)):
        #         if len(wordDict[j]) <= i:
        #             if s[i-len(wordDict[j]):i] == wordDict[j]:
        #                 dp[i] = dp[i-len(wordDict[j])]
        # print(dp)
        # if dp[len(dp)-1] == False:
        #     return []
        dp = [[] for i in range(len(s)+1)]
        def dfs(s, wordDict, index, result, new_string):
            if index==len(s):
                result.append(new_string.strip())
                dp[index] = result
                return dp[index]
            for i in range(len(wordDict)):
                if s[index: index+len(wordDict[i])] == wordDict[i]:
                    result = dfs(s, wordDict, index+len(wordDict[i]), list(result), new_string + ' ' + wordDict[i])
            dp[index] =result
            return dp[index]
        dfs(s, wordDict, 0, [], '')
        return dp[len(s)]