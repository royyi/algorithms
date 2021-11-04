# Roy Yi
# 11/3/21
# Unbounded knapsack (knapsack with repetitions allowed)

import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for i in range(amount+1):
            for j in range(N):
                # either take or don't take option (if possible)
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i-coins[j]] + 1)
                    
        if dp[amount] == float('inf'):
            return -1
        
        return dp[amount]
                
# OPT(n) = min{0..j-1} (OPT(n-coins[j]) + 1)
# dp[i] is the min number of coins needed to make sum i
