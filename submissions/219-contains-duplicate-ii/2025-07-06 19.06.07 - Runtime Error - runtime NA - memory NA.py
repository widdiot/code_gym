class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k == 0:
            return False
        hset = set()
        n = len(nums)
        i, j = 0, min(n-1, k)
        hset = set(nums[i+1:j+1])
        while i < n - 1:
            if nums[i] in hset:
                return True
            i += 1
            hset.remove(nums[i])
            if k < n-1:
                k += 1
                hset.add(nums[k])
        return False
