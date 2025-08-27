class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        for k, v in mydict.items():
            for _ in range(v-1):
                nums.remove(k)
        
        return len(nums)