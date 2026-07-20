class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hmap =  {}
        mfreq = 0
        res = 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            mfreq = max(mfreq, hmap[s[r]])
            num_replacements = r-l+1 - mfreq
            while num_replacements > k:
                hmap[s[l]] -= 1
                l += 1
                mfreq = max(hmap.values())
                num_replacements = r-l+1 - mfreq
            res = max(res, r-l+1)
        return res