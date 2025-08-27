import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            h = 0
            for p in piles:
                h += math.ceil(p/k)
            return h
        i, j = 1, max(piles)
        res = None
        while i <= j:
            mid = (i+j)//2
            if eat(mid) <= h:
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res