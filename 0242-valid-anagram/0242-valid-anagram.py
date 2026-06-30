class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        for i in s:
            smap[i] = smap.get(i, 0) + 1
        tmap = {}
        for i in t:
            tmap[i] = tmap.get(i, 0) + 1
        return smap == tmap