class Solution:
    def __init__(self,):
        self.permutations = []
    def permute(self, nums, prefix):
        if len(nums) == 1:
            self.permutations.append(prefix+nums)
            return
        for i in range(len(nums)):
            self.permute(nums[:i]+nums[i+1:], prefix+[nums[i]])
        return

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        self.permute(sorted_nums, prefix=[])
        print(self.permutations)
        idx = self.permutations.index(nums)
        if idx == len(self.permutations) - 1:
            sol = sorted_nums
        else:
            sol = self.permutations[idx+1]
        for i in range(len(sol)):
            nums[i] = sol[i]