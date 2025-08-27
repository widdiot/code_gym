import re
class Solution:
    def clean(self, s):
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        return s

    def isPalindrome(self, s: str) -> bool:
        s = self.clean(s)
        n = len(s)
        for i in range(n//2):
            if s[i] != s[n-1-i]:
                return False
        return True



        