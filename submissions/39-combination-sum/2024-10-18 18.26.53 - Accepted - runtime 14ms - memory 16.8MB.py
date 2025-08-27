class Solution:
    def __init__(self,):
        self.combos = []
    def recur(self, arr, k , i, n, prefix):
        if k < 0:
            return
        if i == n:
            if k == 0:
                self.combos.append(prefix)
            return
        self.recur(arr, k-arr[i], i, n, prefix+[arr[i]])
        self.recur(arr, k, i+1, n, prefix)
        return 
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.recur(candidates,target, 0, len(candidates), [])
        return self.combos