class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        res = 0
        while i <= j:
            curr = min(height[i], height[j]) * (j-i)
            res = max(res, curr)
            if height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return res