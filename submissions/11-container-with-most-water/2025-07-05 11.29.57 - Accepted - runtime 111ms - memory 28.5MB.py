class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            water = w*h
            max_water = max(max_water, water)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water

        