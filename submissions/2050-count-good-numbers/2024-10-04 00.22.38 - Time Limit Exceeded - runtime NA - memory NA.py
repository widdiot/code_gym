class Solution:
    def pow(x,y):
        """calculate x ^ y recursively"""
        if y == 0:
            return 1
        if y % 2 == 0:
            return pow(x*x, y/2)
        else:
            return x * pow(x, y-1)
    def countGoodNumbers(self, n: int) -> int:
        num_even = n // 2 + n % 2
        num_odd = n // 2
        return (pow(5,num_even) * pow(4,num_odd)) % (10**9 + 7)
        