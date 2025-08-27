from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        i, j = 0, 0
        while j < len(nums):
            if j - i > k:
                hset.remove(nums[i])
                i += 1
            if nums[j] in hset:
                return True
            hset.add(nums[j])
            j += 1
        return False

         

