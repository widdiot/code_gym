class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        i = 0
        j = len(nums) -1 
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] >= target:
                if nums[mid] == target: 
                    if answer[1] == -1:
                        answer[1] = mid
                        answer[0] = mid
                    else:
                        answer[0] = mid              
                j = mid - 1
            else:
                i = mid + 1
        return answer
        