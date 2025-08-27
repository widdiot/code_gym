import re
class Solution:
    def _isPalindrome(self, s, i ,j):
        if i>=j:
            return True
        if not re.match(r"[a-z\d]", s[i]):
            return self._isPalindrome(s, i+1 ,j)
        elif not re.match(r"[a-z\d]", s[j]):
            return self._isPalindrome(s, i ,j-1)
        elif s[i] != s[j]:
            return False
        else:
            return self._isPalindrome(s, i+1 ,j-1)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        return self._isPalindrome(s, 0 ,len(s)-1)

        