class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = -5000
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == curr:
                del nums[i]
            else:
                curr = nums[i]
        return len(nums)