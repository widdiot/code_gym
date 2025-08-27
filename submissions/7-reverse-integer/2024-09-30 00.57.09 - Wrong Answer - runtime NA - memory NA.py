class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x >= 2**31 -1:
            return 0
        flag = False
        if x < 0:
            x = x * (-1)
            flag = True
        reversed = x % 10
        x = x // 10        
        while x:
            digit = x % 10
            x = x // 10
            reversed = reversed * 10 + digit
        if flag:
            reversed = reversed * (-1)
        return reversed
            
        