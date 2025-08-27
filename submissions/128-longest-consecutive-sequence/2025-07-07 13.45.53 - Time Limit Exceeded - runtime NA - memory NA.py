class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hSet = set(nums)
        maxLen = 0
        for num in nums:
            if num-1 not in hSet:
                currLen = 1
                while num + currLen in hSet:
                    currLen += 1
                maxLen = max(maxLen, currLen)
        return maxLen 
                
