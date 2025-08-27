from collections import defaultdict
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums
        l, i, r = 0, 0, len(nums)-1
        
        while i <= r:
            while i < l:
                i += 1
            while nums[l] == 0:
                i += 1
                l += 1
            while nums[r] == 2:
                r -= 1
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i += 1
            else:
                i += 1
            print(nums)
            

            