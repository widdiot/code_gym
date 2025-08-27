class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        res = 5000
        while i <= j:
            mid = (i+j)//2
            if nums[mid] <= nums[j]:
                if nums[mid] < res:
                    res = nums[mid]
                j = mid - 1
            else:
                i = mid + 1
        return res