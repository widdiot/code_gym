class Solution:
    def merge(self, a, b):
        res = []
        i, j = 0, 0 
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        res.extend(a[i:])
        res.extend(b[j:])
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))


        