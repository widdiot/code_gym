class Solution:
    def __init__(self,):
        self.subs = []
    def _subsets(self, nums):
        if nums not in self.subs:
            self.subs.append(nums)
        if not nums:
            return
        for i in range(len(nums)):
            self.subsets(nums[:i]+nums[i+1:])
        return
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self._subsets(nums)
        return self.subs
        