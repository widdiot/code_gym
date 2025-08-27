class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-1):
            if nums[i] in set(nums[i+1:i+k+1]):
                return True
        return False