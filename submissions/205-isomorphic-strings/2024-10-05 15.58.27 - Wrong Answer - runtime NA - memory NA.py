class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mydict = {}
        for i, j in zip(s,t):
            if i != j:
                if i not in mydict:
                    mydict[i] = j
                elif mydict[i] != j:
                    return False
        return True
        