class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            if  num-1 not in hset:
                count = 1
                while num+1 in hset:
                    count += 1
                    num += 1
                if res < count:
                    res = count
            i += 1
        return res
