# binary exponentiation iterative
class Solution:
    def pow(self, x, n):
        ans = 1
        while n != 0:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                ans *= x
                n -= 1 
        return ans
    def myPow(self, x: float, n: int) -> float:
        sol = 1
        neg = False
        if n < 0:
            neg = True
        n = abs(n)
        sol = self.pow(x, n)
        if neg:
            sol = 1/sol
        return sol