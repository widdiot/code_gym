class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1 
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # look left
                j = mid - 1
            else:
                # look right
                i = mid + 1
        return -1