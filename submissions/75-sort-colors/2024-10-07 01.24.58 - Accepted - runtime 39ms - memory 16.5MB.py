class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in range(len(nums)):
            if i < freq.get(0,0):
                nums[i] = 0
            elif i - freq.get(0,0) < freq.get(1,0):
                nums[i] = 1
            elif i - (freq.get(0,0) + freq.get(1,0)) < freq.get(2,0):
                nums[i] = 2


        