class Solution:
    
    def pow(self,x,y,mod):
        """calculate x ^ y iteratively"""
        ans = 1
        while y!=0:
            if y % 2 == 0:
                x *= x
                x %= mod
                y /= 2
            else:
                ans *= x
                ans %= mod
                y -= 1 
        return ans
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9 + 7)
        num_even = n // 2 + n % 2
        num_odd = n // 2
        return (self.pow(5,num_even,mod) * self.pow(4,num_odd,mod)) % mod
        