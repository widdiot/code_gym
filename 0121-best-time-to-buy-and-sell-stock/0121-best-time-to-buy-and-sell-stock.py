class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 10**4
        res = -1
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            if prices[i] - low > res:
                res = prices[i] - low
        return res