class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        def twoSum(arr, target, i, j):
            res = []
            while i < j:
                if arr[i] + arr[j] == target:
                     res.append([arr[i], arr[j]])
                     i += 1
                     j -= 1
                elif arr[i] + arr[j] > target:
                    j -= 1
                else:
                    i += 1
            return res
        
        nums = sorted(nums)
        res = set()
        for i in range(len(nums)):
            ts = twoSum(nums, -nums[i], i+1, len(nums)-1)
            for x in ts: 
                x.append(nums[i])
                res.add(tuple(x))
        return [list(t) for t in res]
        