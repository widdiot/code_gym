class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, profit = 10**4, 0
        for i in range(len(prices)):
            mini = min(prices[i], mini)
            curr_profit = prices[i] - mini
            profit = max(curr_profit, profit)
        return profit
        
        