class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0
        while left < right:
            res = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, res)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
        return max_area
        



        