class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        a = []
        maxlen = 0
        currlen = 0
        for i in range(len(s)):
            if s[i] not in hset:
                hset.add(s[i])
                currlen += 1
                maxlen = max(maxlen, currlen)
            else:
                # reset
                currlen = 0
                hset.clear()
                # account for current
                currlen += 1
                hset.add(s[i])
        return maxlen
        