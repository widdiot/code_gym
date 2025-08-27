class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hSet = set(nums)
        maxLen = 0
        currLen = 0
        for i in range(len(nums)):
            num = nums[i]
            if num-1 not in hSet:
                currLen = 1
                num += 1 
                while num in hSet:
                    currLen += 1
                    num += 1
                maxLen = max(maxLen, currLen)
        return maxLen 
                
