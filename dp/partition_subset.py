# Roy Yi
# 11/3/21
# partition equal subset sum

class Solution:     
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        
        N = len(nums)
        target = total // 2
        
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(1, N+1):
            for j in range(target, 0, -1):
                if j - nums[i-1] >= 0:
                    dp[j] = dp[j-nums[i-1]] or dp[j]
            
        return dp[target] == 1
        
# can a subset of numbers be chosen to hit a target?
# achieve a total sum exact as capacity

# dp[i][j] is true if we can sum to target j with elements nums{0..i-1}
# false otherwise

# space optimized version: use 1d array and compute in reverse order
# for current row, we can use prior row values as we compute right to left
