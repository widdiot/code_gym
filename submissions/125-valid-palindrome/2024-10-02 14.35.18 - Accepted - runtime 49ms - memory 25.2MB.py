import re
class Solution:
    def clean(self, s):
        s = re.sub(r"[^a-z0-9]", "", s.lower())
        return s

    def recur(self, s, i, j):
        if i >= j:
            return True
        if s[i] == s[j]:
            return self.recur(s, i+1, j-1)
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = self.clean(s)
        return self.recur(s, 0, len(s)-1)



        