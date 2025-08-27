class Solution:
    def permute(self, counts, prefix, result):
        if sum(counts.values()) == 0:
            result.append(prefix)
            return

        for i in counts.keys():
            if counts[i] > 0:
                counts[i] -= 1
                self.permute(counts, prefix+[i], result)
                counts[i] += 1
        return

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        counts = {}
        for i in nums:
            counts[i] = counts.get(i,0) + 1 

        prefix, result = [], []
        self.permute(counts, prefix, result)
        return result
