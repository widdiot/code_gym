class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        res = len(nums)
        while i <= j:
            mid = (i+j)//2
            if target <= nums[mid]:
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res