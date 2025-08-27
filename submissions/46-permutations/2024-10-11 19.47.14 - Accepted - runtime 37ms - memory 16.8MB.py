class Solution:
    def __init__(self,):
        self.permutations = []
    def print_perms(self, nums, prefix):
        if len(nums) == 1:
            self.permutations.append(prefix + nums)
            return
        for i in range(len(nums)):
            self.print_perms(nums[:i]+nums[i+1:], prefix + [nums[i]])
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.print_perms(nums, [])
        return self.permutations


        