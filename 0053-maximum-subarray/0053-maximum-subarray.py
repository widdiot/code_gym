class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = float("-inf")
        for i in range(len(nums)):
            if s < 0:
                s = 0
            s += nums[i]
            if res < s:
                res = s
        return res