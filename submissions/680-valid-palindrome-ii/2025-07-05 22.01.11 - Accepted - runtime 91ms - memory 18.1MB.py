class Solution:
    def isPalindrome(self, s: list, i: int) -> bool:
        del s[i]
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(list(s), l) or self.isPalindrome(list(s), r)
            l += 1
            r -= 1
        return True   
        