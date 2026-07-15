class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(hmap,tmap):
            for c in tmap:
                if c not in hmap or hmap[c] < tmap[c]:
                    return False
            return True

        tmap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1
        l = 0
        hmap = {}
        minlen = float("inf")
        res = [0,0]
        for r in range(len(s)):
            if s[r] in tmap:
                hmap[s[r]] = hmap.get(s[r], 0) + 1
            while is_valid(hmap, tmap):
                if r-l+1 < minlen:
                    minlen = r-l+1
                    res = [l,r+1]
                if s[l] in hmap:
                    hmap[s[l]] -= 1
                l += 1

        return s[res[0]:res[1]]


