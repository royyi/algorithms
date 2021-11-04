# Roy Yi
# 11/3/21
# Nonadjacent subset sum

class Solution:
    def find_subset(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]

        N = len(nums)
        r = [0] * N

        r[0] = nums[0]
        r[1] = max(nums[0], nums[1])

        for i in range(2, N):
            r[i] = max(r[i-1], r[i-2] + nums[i])

        return r[N-1]


# recurrence: OPT(arr{n}) = max( OPT(arr{n-1}), OPT(arr{n-2} + arr[n]) )
# either we take the last element in the set, or we exclude it from the set

# r[i] represents maximum sum for arr ending at i
