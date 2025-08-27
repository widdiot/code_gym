class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = -10**4
        for i in nums:
            sum += i
            maxsum = max(sum, maxsum)
            sum = max(0, sum)
        return maxsum
            
                
        