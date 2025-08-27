class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            vector = [0] * 26
            for i in s:
                vector[ord(i) - ord("a")] += 1
            hmap[tuple(vector)].append(s)
        return list(hmap.values())

        