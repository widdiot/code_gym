class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            if count > 0 and nums[i] != 1:
                if count > max_count:
                    max_count = count 
                count = 0
            i += 1
        if count > max_count:
            max_count = count
        return max_count
        