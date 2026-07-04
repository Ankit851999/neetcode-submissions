class Solution:
    def trap(self, height) :
        left = 0
        right = 1
        length = len(height)
        lisst = set()
        temp = 0
        while right < length:
            if height[left] > height[right]:
                temp += height[left] - height[right]
                right += 1
            else:
                lisst.add((left, right, temp))
                left = right 
                right = left + 1
                temp = 0
        right = length -1
        left = right -1
        temp = 0
        while left > -1:
            if height[right] > height[left]:
                temp += height[right] - height[left]
                left -= 1
            else:
                lisst.add((left, right, temp))
                right = left 
                left = right - 1
                temp = 0
        area = 0
        for (i,j, a) in lisst:
            area += a
        return area
