class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        winsum = 0
        i = 0 
        for j in range(len(nums)):
            winsum += nums[j]
            if winsum > res:
                res = winsum
            while winsum < 0:
                winsum -= nums[i]
                i += 1
        return res