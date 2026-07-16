class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            l, r = 0, len(nums)-1
            res, residx = float("inf"), len(nums)
            while l <= r:
                mid = (l+r)//2
                if nums[mid] <= nums[r]:
                    if nums[mid] < res:
                        res = nums[mid]
                        residx = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return residx
        def bs(nums, target, l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        pivot = find_pivot(nums)
        if target >= nums[pivot] and target <= nums[-1]:
            return bs(nums, target, pivot, len(nums)-1)
        return bs(nums, target, 0, pivot-1)
                    
