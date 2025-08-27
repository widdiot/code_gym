class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            hmap[i] = 0
        res = 0
        for i in nums:
            count = 1
            curr = i
            hmap[curr] = 1
            while curr + 1 in hmap:
                count += 1
                curr += 1
                hmap[curr] = 1

            curr = i
            while curr - 1 in hmap:
                count += 1
                curr -= 1
                hmap[curr] = 1

            
            if count > res:
                res = count
        return res
