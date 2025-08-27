class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        currmin = 10**4
        res = 0
        while i < len(prices):
            currmin = min(currmin, prices[i])
            res = max(res, prices[i] - currmin)
            i += 1
        return res


        
        