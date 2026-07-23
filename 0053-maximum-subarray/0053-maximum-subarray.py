class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        res = -float("inf")
        curr = 0 
        for r in range(len(nums)):
            curr += nums[r]
            res = max(curr, res)
            if curr < 0:
                curr = 0
                l = r+1

        return res
            