class Solution:
    def myPow(self, x: float, n: int) -> float:
        sol = 1
        neg = False
        if n < 0:
            neg = True
        n = abs(n)
        for i in range(0,n):
            sol *= x
            if sol >= 10**4:
                break
        if neg:
            sol = 1/sol
        return sol