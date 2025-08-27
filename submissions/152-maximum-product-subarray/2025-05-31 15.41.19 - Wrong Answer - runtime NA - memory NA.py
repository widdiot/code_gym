class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = nums[0]
        minprod = nums[0]
        answer = nums[0]
        for i in range(1,len(nums)):
            if i > 0:
                maxprod *= nums[i]
                minprod *= nums[i]
            elif i < 0:
                maxprod, minprod = minprod, maxprod
                maxprod *= nums[i]
                minprod *= nums[i]
            else:
                if i < len(nums) - 1:
                    maxprod = nums[i+1]
                    minprod = nums[i+1]
                    continue
                
            answer = max(maxprod, answer) 
        return answer
        