class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        coins = sorted(coins)
        dp[0]=0
        for money in range(1, amount+1):
            for coin in coins:
                if money - coin >=0:
                    dp[money] = min(dp[money], 1 + dp[money-coin])
        return dp[amount] if dp[amount] != amount+1 else -1