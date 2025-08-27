class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        hset = set()
        res = 0
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            res = max(res, r - l+1)
        return res


        