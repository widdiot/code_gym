class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            n2 = target - nums[i]
            if n2 in hmap:
                return [i, hmap[n2]]
            hmap[nums[i]] = i 
