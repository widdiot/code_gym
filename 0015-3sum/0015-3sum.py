class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        def twoSum(nums, l, r, target):
            res = []
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([-target, nums[l], nums[r]])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            return res
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tsum = twoSum(nums, i+1, len(nums)-1, -nums[i])
            res.extend(tsum)
        return res