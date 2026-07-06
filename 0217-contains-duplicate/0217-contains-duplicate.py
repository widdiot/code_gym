class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for i in range(len(nums)):
            if nums[i] in hset:
                return True
            hset.add(nums[i])
        return False