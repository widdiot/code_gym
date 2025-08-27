class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            Sum = max(0, Sum)
            if Sum > max_sum:
                max_sum = Sum
        return max_sum
