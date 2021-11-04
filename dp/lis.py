# Roy Yi
# 11/3/21
# Find longest increasing subsequence of integer array

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1]*N
        
        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                       
        return max(dp)
    
# dp[i] is the maximum length for the subsequence ending with arr[i]
        
# L[i] = 1 + max(L[j]) from 0 <= j < i such that arr[j] < arr[i]
# 1 if no such j exists
