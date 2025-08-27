class Solution:
    def __init__(self,):
        self.permutations = []
        self.permutations_set = set()
    def permute(self, nums, prefix):
        if len(nums) == 1:
            if tuple(prefix+nums) not in self.permutations_set:
                self.permutations.append(prefix+nums)
                self.permutations_set.add(tuple(prefix+nums))
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
        idx = self.permutations.index(nums)
        sol = self.permutations[(idx+1)%len(self.permutations)]
        for i in range(len(sol)):
            nums[i] = sol[i]