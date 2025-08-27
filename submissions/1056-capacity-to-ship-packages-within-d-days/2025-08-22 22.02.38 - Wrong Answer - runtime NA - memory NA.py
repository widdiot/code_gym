class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i, j  = max(weights), sum(weights)
        def num_days(capacity):
            load, days = 0, 0
            for w in weights:
                if load + w <= capacity:
                    load += w
                else:
                    days += 1
            return days
        res = j
        while i<=j:
            mid = (i+j)//2
            d = num_days(mid)
            if d <= days:
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res