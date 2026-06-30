class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, l = 0, 0
        res = 0
        hset = set()
        for j in range(len(s)):
            while s[j] in hset:
                hset.remove(s[i])
                i += 1
                l -= 1
            hset.add(s[j])
            l += 1
            if l > res:
                res = l
        return res