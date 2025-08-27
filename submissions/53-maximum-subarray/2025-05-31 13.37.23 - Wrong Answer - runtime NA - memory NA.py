class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = -10**4
        for i in nums:
            sum += i
            sum = max(0, sum)
            maxsum = max(sum, maxsum)
        return maxsum
            
                
        