class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i,h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = max(area, ( i -index) * height)
                start = index
            
            stack.append((start, h))
        for i,h in stack:
            area = max(area, (len(heights) -i) * h)
        return area