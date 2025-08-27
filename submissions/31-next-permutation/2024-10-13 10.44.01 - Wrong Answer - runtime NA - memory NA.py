class Solution:


    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breaker = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                breaker = i
                break
        if breaker == None:
            nums.reverse()
        else:
            
            min_idx = breaker+1+nums[breaker+1:].index(min(nums[breaker+1:]))
            print(min_idx)
            nums[breaker], nums[min_idx] = nums[min_idx], nums[breaker]
            print(nums)
            nums[breaker+1:] = sorted(nums[breaker+1:]) 
            print(nums)