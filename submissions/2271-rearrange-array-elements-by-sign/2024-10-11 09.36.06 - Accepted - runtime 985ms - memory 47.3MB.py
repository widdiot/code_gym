class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        p, n = 0, 1
        for i in range(N):
            if nums[i] >= 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2
        return ans