class Solution:
    def isPalindrome(self, s: str, i: int) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if l == i:
                l += 1
            elif r == i:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l) or self.isPalindrome(s, r)
            r -= 1
            l += 1
        return True
        