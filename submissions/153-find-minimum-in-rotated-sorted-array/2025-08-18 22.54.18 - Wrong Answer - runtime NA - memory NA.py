class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        res = 0
        while i <= j:
            mid = (i+j)//2
            if nums[mid] <= nums[j]:
                res = nums[mid]
                j = mid - 1
            else:
                i = mid + 1
        return res