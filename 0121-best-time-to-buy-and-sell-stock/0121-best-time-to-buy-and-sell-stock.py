class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = 10**4
        res = 0
        for i in prices:
            cmin = min(cmin, i)
            res = max(res, i-cmin)
        return res