class Solution:
    def pow(x,y):
        """calculate x ^ y iteratively"""
        ans = 1
        while y!=0:
            if y % 2 == 0:
                x *= x
                n /= 2
            else:
                ans *= x
                n -= 1 
        return ans
    def countGoodNumbers(self, n: int) -> int:
        num_even = n // 2 + n % 2
        num_odd = n // 2
        return (pow(5,num_even) * pow(4,num_odd)) % (10**9 + 7)
        