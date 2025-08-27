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
        
        if not breaker:
            nums.reverse()
        else:
            print(breaker)
            min_idx = breaker+1+nums[breaker+1:].index(min(nums[breaker+1:]))
            print(min_idx)
            nums[breaker], nums[min_idx] = nums[min_idx], nums[breaker]
            print(nums)
            nums[breaker+1:] = sorted(nums[breaker+1:]) 
            print(nums)