class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = nums[0]
        minprod = nums[0]
        answer = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] > 0:
                maxprod *= nums[i]
                minprod *= nums[i]
                answer = max(maxprod, answer)
                i += 1
            elif nums[i] < 0:
                maxprod, minprod = minprod, maxprod
                maxprod *= nums[i]
                minprod *= nums[i]
                answer = max(maxprod, answer) 
                i += 1
            else:
                maxprod *= nums[i]
                minprod *= nums[i]
                answer = max(maxprod, answer) 
                if i < len(nums) - 1:
                    maxprod = nums[i+1]
                    minprod = nums[i+1]
                i += 2
                
            
        return answer
        