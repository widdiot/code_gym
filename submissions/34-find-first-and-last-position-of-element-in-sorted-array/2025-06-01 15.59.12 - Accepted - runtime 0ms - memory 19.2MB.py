class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        i = 0
        j = len(nums) -1
        # find the inf
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    answer[0] = mid
                j = mid - 1
            else:
                i = mid + 1
        # find the sup
        i = 0
        j = len(nums) -1
        while i <= j:
            mid = i + (j - i) // 2 
            if nums[mid] <= target:
                if nums[mid] == target:
                    answer[1] = mid
                i = mid + 1
            else:
                j = mid - 1
        return answer
        