from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting method
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        
        idx = 0
        for i in range(3):
            while hmap[i] > 0:
                nums[idx] = i
                hmap[i] -= 1
                idx += 1