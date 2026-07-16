class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for n in hset:
            if n-1 not in hset:
                count = 0
                while n in hset:
                    count += 1
                    n += 1
                res = max(count, res)
        return res
                
