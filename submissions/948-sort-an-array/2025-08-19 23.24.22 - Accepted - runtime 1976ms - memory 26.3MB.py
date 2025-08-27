class Solution:
    def merge(self, a, b):
        res = []
        while a or b:
            if not a:
                res.append(b.pop(0))
            elif not b:
                res.append(a.pop(0))
            else:
                if a[0] <= b[0]:
                    res.append(a.pop(0))
                else:
                    res.append(b.pop(0))
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = len(nums)//2
        return self.merge(self.sortArray(nums[:mid]), self.sortArray(nums[mid:]))


        