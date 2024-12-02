class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Recursive approach:
        1. Find at every index whether the word can be broken into a else move forward with the index
        2. base condition if index > length of string then return false
        3. we need to find the condition to return true


        Memoization:
        keep a one dimensional array of size n+1 where n is the size of the list.
        store the recursive call in the array index
        and then return it

        Top down approach:
        same thing but without recursion.
         wordDict = set(wordDict)
        dp = [None]*(len(s)+1)
        dp[0] = True
        def recursion(target: str):
            if not target:
                return True
            for i in range(len(target)):
                if target[:i+1] in wordDict and recursion(target[i+1:]):
                    dp[i] = True
                    return dp[i]
                else:
                    dp[i] = False
            dp[-1] = False
            return dp[-1]
        return recursion(s)
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(len(s)+1):
            for word in wordDict:
                if i >= len(word) and s[i-len(word):i] == word:  
                    dp[i] = dp[i-len(word)] or dp[i]
        return dp[-1]
        
       

