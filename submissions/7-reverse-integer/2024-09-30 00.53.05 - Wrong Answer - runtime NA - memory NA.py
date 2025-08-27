class Solution:
    def reverse(self, x: int) -> int:
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
            
        