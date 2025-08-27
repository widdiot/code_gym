class Solution:
    def print_perms(self, nums, prefix, results):
        if len(nums) == 1:
            results.append(prefix + nums)
            return
        for i in range(len(nums)):
            self.print_perms(nums[:i]+nums[i+1:], prefix + [nums[i]], results)
        return

    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        self.print_perms(nums, [], results)
        return results


        