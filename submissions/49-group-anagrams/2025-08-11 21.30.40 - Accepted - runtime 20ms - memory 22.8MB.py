from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            vec = [0]*26
            for i in s:
                vec[ord(i)-ord('a')] += 1
            res[tuple(vec)].append(s)
        return list(res.values())