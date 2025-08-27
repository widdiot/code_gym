class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        res = 0
        while i <= j:
            mid = (i+j)//2
            sq = mid ** 2
            if x >= sq:
                res = mid
                i = mid + 1
            else:
                j = mid - 1
        return res