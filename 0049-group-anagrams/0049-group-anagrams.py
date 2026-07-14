class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hmap = {}
        for i in range(len(strs)):
            arr = [0] * 26
            for c in strs[i]:
                arr[ord(c)-97] += 1
            if tuple(arr) in hmap:
                hmap[tuple(arr)].append(strs[i])
            else:
                hmap[tuple(arr)] = [strs[i]]
        return list(hmap.values())