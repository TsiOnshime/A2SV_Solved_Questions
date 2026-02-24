class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0
        l, r = 0, len(height) - 1

        while l < r:
            width = r - l
            min_height = min(height[l], height[r])

            area = min_height * width

            max_container = max(max_container, area)

            if height[l] <= height[r]:
                l += 1
            else: 
                r -= 1
        return max_container
