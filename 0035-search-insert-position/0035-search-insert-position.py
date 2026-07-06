class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        res = len(nums)
        while low <= high:
            mid = (low+high)//2
            if target <= nums[mid]:
                res = mid
                high = mid -1
            else:
                low = mid + 1
        return res