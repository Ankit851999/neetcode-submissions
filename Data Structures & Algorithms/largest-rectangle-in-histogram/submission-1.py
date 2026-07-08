class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        highestBar = heights[0]
        lastZero = -1
        
        maxArea = heights[0]

        for i in range(0, len(heights)):
            if heights[i] == 0:
                continue
            if heights[i] == 7:
                print(True)
            minHeight = heights[i]
            area = heights[i]
            maxWidth = 1
            left, right = i,i
            while left> -1 and right < len(heights) and (heights[left] != 0 or heights[right] != 0) :
                if left - 1 > -1 and right + 1 < len(heights):
                    if heights[left -1] > heights[right +1 ]:
                        left -= 1
                        minHeight = min(minHeight, heights[left]) 
                    else:
                        right += 1  
                        minHeight = min(minHeight, heights[right]) 
                elif left - 1 > -1 and right + 1 >= len(heights):
                        left -= 1
                        minHeight = min(minHeight, heights[left]) 
                elif right + 1 < len(heights):
                    right += 1
                    minHeight = min(minHeight, heights[right]) 
                else:
                    break
                maxWidth += 1
                area = max(area, minHeight *maxWidth)
            maxArea = max(maxArea, area)
        return maxArea