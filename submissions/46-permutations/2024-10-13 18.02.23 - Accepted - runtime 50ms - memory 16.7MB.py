class Solution:
    def _perms(self, nums, idx, n):
        if idx == n:
            return [[]]
        prefix = nums[idx]
        perms =  self._perms(nums, idx+1, n)
        res = []
        for i in range(len(perms)):
            for j in range(len(perms[i])+1):
                p_copy = perms[i].copy()
                p_copy.insert(j, prefix)
                res.append(p_copy)
        return res

    def permute(self, nums: List[int]) -> List[List[int]]:
        idx = 0
        n = len(nums)
        res = self._perms(nums, idx, n)
        return res


        