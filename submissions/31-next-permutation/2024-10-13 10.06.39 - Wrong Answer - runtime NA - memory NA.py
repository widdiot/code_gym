class Solution:
    def __init__(self,):
        self.permutations = []
        self.permutations_set = set()
    def permute(self, nums, prefix):
        if len(self.permutations_set) == 2:
            return
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
        descending = True
        prev_i = 101
        for i in nums:
            if i > prev_i:
                descending = False
                break
            prev_i = i

        if not descending:
            self.permute(nums, prefix=[])
            sol = self.permutations[-1]
        else:
            sol = sorted(nums)
        
        for i in range(len(sol)):
            nums[i] = sol[i]