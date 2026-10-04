class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        left = 0
        right = len(heights) -1
        while left < right:
            lenght = right - left
            if heights[left] > heights[right]:
                area = max(area, lenght * heights[right])
                right -= 1
            elif heights[right] > heights[left]:
                area = max(area, lenght * heights[left])
                left += 1
            else:
                area = max(area, lenght * heights[left])
                if left +1 != right -1:
                    if heights[left +1] > heights[right -1]:
                        left += 1
                    else:
                        right -= 1
                else:
                    break
        return area



