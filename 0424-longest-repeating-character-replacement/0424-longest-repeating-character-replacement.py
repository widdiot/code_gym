class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0 
        l, r = 0, 0 
        res = 0
        hmap, maxfreq, numreplace = {}, 0, 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            maxfreq = max(maxfreq, hmap[s[r]])
            numreplace = r-l+1 - maxfreq
            while numreplace > k:
                hmap[s[l]] -= 1
                maxfreq = max(hmap.values())
                l += 1
                numreplace = r-l+1 - maxfreq
            res = max(res, r-l+1)
        return res