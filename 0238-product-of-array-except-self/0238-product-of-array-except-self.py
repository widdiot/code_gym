class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pprod = 1
        res = [1]* len(nums)
        for i in range(len(nums)):
            res[i] *= pprod
            pprod *= nums[i]

        sprod = 1
        for i in range(len(nums)):
            res[len(nums)-1-i] *= sprod
            sprod *= nums[len(nums)-1-i]

        return res
        