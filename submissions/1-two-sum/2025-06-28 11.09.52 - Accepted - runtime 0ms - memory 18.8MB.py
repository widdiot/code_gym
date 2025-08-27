class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_keys = sorted(range(len(nums)), key=lambda x: nums[x])
        i, j = 0, len(nums)-1
        while i<j:
            if nums[sorted_keys[i]] + nums[sorted_keys[j]] < target:
                i += 1
            elif nums[sorted_keys[i]] + nums[sorted_keys[j]] > target:
                j -= 1
            else:
                break
        return [sorted_keys[i], sorted_keys[j]]