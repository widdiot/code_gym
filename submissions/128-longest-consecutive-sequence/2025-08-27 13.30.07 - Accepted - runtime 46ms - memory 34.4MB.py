class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for num in hset:
            if  num-1 not in hset:
                count = 1
                while num+count in hset:
                    count += 1
                res = max(res,count)
        return res
