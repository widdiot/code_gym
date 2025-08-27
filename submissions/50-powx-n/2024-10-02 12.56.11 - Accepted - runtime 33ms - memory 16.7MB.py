# binary exponentiation
class Solution:
    def pow(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.pow(x*x, n/2)
        elif n % 2 != 0:
            return x * self.pow(x, n-1)
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