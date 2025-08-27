class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pref = ""
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i > len(s) - 1 or s[i] != strs[0][i]:
                    return pref
            pref += strs[0][i]
        return pref