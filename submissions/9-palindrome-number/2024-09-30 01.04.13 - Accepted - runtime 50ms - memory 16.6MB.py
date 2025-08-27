class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        if x < 0:
            return False
        reversed = x % 10
        x = x // 10
        while x:
            digit = x % 10
            x = x // 10
            reversed = reversed * 10 + digit
        return reversed == original

        