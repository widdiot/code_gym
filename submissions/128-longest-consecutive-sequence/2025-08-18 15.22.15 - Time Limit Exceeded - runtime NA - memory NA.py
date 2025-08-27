class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set()
        for i in nums:
            hset.add(i)
        res = 0
        for i in nums:
            count = 1
            curr = i
            while curr + 1 in hset:
                count += 1
                curr += 1

            curr = i
            while curr - 1 in hset:
                count += 1
                curr -= 1
            
            if count > res:
                res = count
        return res
