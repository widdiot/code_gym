class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        answer = len(nums)
        while i <= j:
            mid = i + (j - i) //2
            if nums[mid] >= target:
                answer = mid
                # look left
                j = mid - 1
            else:
                i = mid + 1
        return answer