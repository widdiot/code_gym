class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                hset.remove(nums[L])
                L += 1
            if nums[R] in hset:
                return True
            hset.add(nums[R])
        return False
