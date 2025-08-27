class Solution:
    def __init__(self,):
        self.sol = []

    def recur(self, arr, i, n, k, p):
        if i >= n:
            if k == 0:
                self.sol.append(p)
            return 
        self.recur(arr, i+1, n, k-arr[i], p+[arr[i]])
        while i+1 < n and arr[i] == arr[i+1]:
            i += 1
        self.recur(arr, i+1, n, k, p)
        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        self.recur(candidates, 0, len(candidates), target, [])
        return self.sol