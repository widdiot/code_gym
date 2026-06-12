class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(low, high):
            if low > high:
                return -1
            mid = (low+high)//2
            if nums[mid] == target:
                print("Xxx")
                return mid
            elif target < nums[mid]:
                return bs(low, mid-1)
            else:
                return bs(mid+1, high)
            return -1
        return bs(0, len(nums)-1)