class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        myset = set()
        del_indices = []
        for i in range(len(nums)):
            if nums[i] in myset:
                del_indices.append(i)
            else:
                myset.add(nums[i])
        for i in sorted(del_indices, reverse=True):
            del nums[i]
        return len(nums)