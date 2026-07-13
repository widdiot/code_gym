class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = {}
        prod = 1
        for i in range(len(nums)):
            prefix_prod[i] = prod
            prod *= nums[i]
        
        suffix_prod = {}
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            suffix_prod[i] = prod
            prod *= nums[i]
        
        return [prefix_prod[i]*suffix_prod[i] for i in range(len(nums))]
        