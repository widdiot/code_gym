class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix_len = 0
            j = 0
            while j < min(len(prefix),len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                prefix_len += 1
                j += 1
            prefix = prefix[:prefix_len]
        return prefix
