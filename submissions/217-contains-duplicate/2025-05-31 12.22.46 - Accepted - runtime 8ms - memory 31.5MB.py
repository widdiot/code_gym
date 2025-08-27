class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = set()
        for i in nums:
            if i not in uniq:
                uniq.add(i)
            else:
                return True
        return False