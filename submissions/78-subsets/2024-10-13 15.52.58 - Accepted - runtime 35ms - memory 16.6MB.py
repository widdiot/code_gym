class Solution:

    def _subsets(self, nums, idx, n, prefix, results):
        if idx == n:
            results.append(prefix)
            return 
        self._subsets(nums, idx+1, n, prefix+[nums[idx]], results)
        self._subsets(nums, idx+1, n, prefix, results)
        return 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        prefix = []
        idx = 0
        n = len(nums)
        self._subsets(nums, idx, n, prefix, results)
        return results
        