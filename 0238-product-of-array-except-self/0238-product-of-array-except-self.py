class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = {}
        suffix_prod = {}
        pprod = 1
        sprod = 1
        for i in range(len(nums)):
            prefix_prod[i] = pprod
            pprod *= nums[i]
            suffix_prod[len(nums)-1-i] = sprod
            sprod *= nums[len(nums)-1-i]

        return [prefix_prod[i]*suffix_prod[i] for i in range(len(nums))]
        