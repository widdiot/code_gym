class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = 10**4
        minidx = 0
        maxi = 0
        maxidx = 0
        profit = 0
        for i, p in enumerate(prices):
            if p < mini:
                mini = p
                minidx = i
            if p > maxi and i > minidx:
                maxi = p
                maxidx = i
            profit = max(profit , maxi - mini)
        return profit
        
        