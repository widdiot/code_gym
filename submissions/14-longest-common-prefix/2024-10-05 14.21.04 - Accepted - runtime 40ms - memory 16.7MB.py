class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key = lambda x: len(x))
        i = 0
        flag = False
        while i < len(smallest):
            c = smallest[i]
            print(c)
            for j in strs:
                print(j[i])
                if j[i] != c:
                    flag = True
                    break
            if flag:
                break
            i += 1
        return smallest[:i]