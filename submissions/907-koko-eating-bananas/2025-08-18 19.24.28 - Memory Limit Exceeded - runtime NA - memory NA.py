import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(k):
            h = 0
            for p in piles:
                h += math.ceil(p/k)
            return h
        speeds = list(range(1, max(piles)+1))
        i, j = 0, len(speeds)-1
        res = None
        while i <= j:
            mid = (i+j)//2
            if eat(speeds[mid]) == h:
                res = speeds[mid]
                j = mid - 1
            elif eat(speeds[mid]) < h:
                j = mid - 1
            else:
                i = mid + 1
        return res