import re
class Solution:
    def _isPalindrome(self, s, i ,j):
        if i>=j:
            return True
        if not re.match(r"[a-z]", s[i].lower()):
            return self._isPalindrome(s, i+1 ,j)
        elif not re.match(r"[a-z]", s[j].lower()):
            return self._isPalindrome(s, i ,j-1)
        elif s[i].lower() != s[j].lower():
            return False
        else:
            return self._isPalindrome(s, i+1 ,j-1)

    def isPalindrome(self, s: str) -> bool:
        return self._isPalindrome(s, 0 ,len(s)-1)

        