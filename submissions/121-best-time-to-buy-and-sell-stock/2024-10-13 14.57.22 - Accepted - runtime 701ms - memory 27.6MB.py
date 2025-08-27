class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = prices[0]
        diff = 0
        for i in range(len(prices)):
            if prices[i] > minn:
                if prices[i] - minn > diff:
                    diff = prices[i] - minn
            else:
                minn = prices[i]
        return diff