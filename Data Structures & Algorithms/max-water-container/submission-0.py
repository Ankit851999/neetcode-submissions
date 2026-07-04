class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        length = len(heights)
        left = 0
        right = length -1
        while left < right:
            maxvol = max(maxvol, min(heights[left], heights[right]) * (right-left))
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return maxvol
            
