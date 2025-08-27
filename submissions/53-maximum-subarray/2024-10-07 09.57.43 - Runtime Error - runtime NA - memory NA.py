class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -1)**4
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum > max_sum:
                max_sum = Sum
            Sum = max(0, Sum)
        return max_sum
