class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for i in nums:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)

        p, n = 0, 0 
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = pos[p]
                p += 1
            else:
                nums[i] = neg[n]
                n += 1
        return nums