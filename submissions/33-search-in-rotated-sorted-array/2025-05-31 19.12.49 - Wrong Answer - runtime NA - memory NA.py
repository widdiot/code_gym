class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = i + (j-i)//2
            if nums[mid] == target:
                return mid
            print(nums[i:j+1], mid)
            if nums[mid] > nums[i]:
                if target >= nums[i] and target <= nums[mid]:
                    j = mid
                else:
                    i = mid + 1
            else:
                if target >= nums[mid] and target <= nums[j]:
                    i = mid
                else:
                    j = mid -1
        return -1