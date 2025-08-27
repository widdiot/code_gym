class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = sorted(range(len(nums)), key=lambda x: nums[x])
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[indices[i]]+nums[indices[j]] >target:
                j -= 1
            elif nums[indices[i]]+nums[indices[j]] < target:
                i += 1
            else:
                return [indices[i], indices[j]]