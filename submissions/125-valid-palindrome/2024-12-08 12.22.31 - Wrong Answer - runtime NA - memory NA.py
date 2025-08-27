import re
class Solution:
    def _isPalindrome(self, s, i ,j):
        if i>=j:
            return True
        if s[i] != s[j]:
            return False
        else:
            return self._isPalindrome(s, i+1 ,j-1)

    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[\s,:\.;\'\"{}\]\[!@#$%\^&\*_+=\-]","",s.lower())
        print(s)
        return self._isPalindrome(s, 0 ,len(s)-1)

        