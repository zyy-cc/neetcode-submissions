class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, len(height) - 1
        left_most = right_most = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_most:
                    left_most = height[left]
                else:
                    total += left_most - height[left]
                left += 1
            else:
                if height[right] >= right_most:
                    right_most = height[right]
                else:
                    total += right_most - height[right]
                right -= 1
        return total
        