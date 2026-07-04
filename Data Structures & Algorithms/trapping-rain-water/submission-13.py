class Solution:
    def trap(self, height) :
        n = len(height)
        leftmax = 0
        rightmax = n-1
        water = 0
        left = 0
        right = n -1

        while left < right:
            if height[left] < height[right]:
                if height[left] >= height[leftmax]:
                    leftmax = left
                else:
                    water += height[leftmax] -height[left]
                left += 1
            else:
                if height[right] >= height[rightmax]:
                    rightmax = right
                else:
                    water += height[rightmax] -height[right]
                right -= 1
        return water
