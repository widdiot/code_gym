class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            vector = [0] * 26
            for i in s:
                vector[ord(i) - ord("a")] += 1
            if tuple(vector) in hmap:
                hmap[tuple(vector)].append(s)
            else:
                hmap[tuple(vector)] = [s]
        return list(hmap.values())

        