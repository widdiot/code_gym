class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        currmin = 10**4
        res = 0
        while i < len(prices):
            if prices[i] < currmin:
                currmin = prices[i]
            if prices[i] - currmin > res:
                res = prices[i] - currmin
            i += 1
        return res


        
        