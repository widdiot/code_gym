class Solution:
    def countGoodNumbers(self, n: int) -> int:
        num_even = n // 2 + n % 2
        num_odd = n // 2
        return (5**num_even * 4**num_odd) % (10**9 + 7)
        