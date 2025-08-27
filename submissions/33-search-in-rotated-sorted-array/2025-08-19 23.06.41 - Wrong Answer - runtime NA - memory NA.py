class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_pivot(nums):
            i, j = 0, len(nums)-1
            mini = 10**4
            minidx = -1
            while i <= j:
                mid = (i+j)//2
                if nums[mid] < mini:
                    mini = nums[mid]
                    minidx = mid
                if nums[mid] <= j:
                    j = mid - 1
                else:
                    i = mid + 1
            return minidx
        
        minidx = find_pivot(nums)

        i, j = minidx, minidx + len(nums) - 1
        while i <= j:
            mid = (i+j)//2
            real_mid = mid%len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1

            
            