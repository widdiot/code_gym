class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = -1, -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if target <= nums[mid]:
                if nums[mid] == target:
                    i = mid
                high = mid - 1
            else:
                low = mid + 1

        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    j = mid
                low = mid + 1
            else:
                high = mid - 1
        return [i, j]