class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, m*n-1
        def getIdx(i):
            return [i//n, i%n] 
        while i <= j:
            mid = (i+j)//2
            idx = getIdx(mid)
            if matrix[idx[0]][idx[1]] == target:
                return True
            elif matrix[idx[0]][idx[1]] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False