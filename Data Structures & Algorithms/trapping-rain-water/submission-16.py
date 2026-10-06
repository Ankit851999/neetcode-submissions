class Solution: 
    def trap(self, height):
        n = len(height)
        if n in [ 0,1,2]:
            return 0
        l = 0
        r = len(height) -1
        mh = 0
        a = 0 
        while r-l > 1:
            mhl = min(height[l], height[r])
            if mhl > mh:
                a += ((mhl -mh) * (r-l-1))
                mh = mhl
            if height[l] < height[r]:
                l += 1
                a -= min(height[l],mh )
            else:
                r -= 1
                a -= min(height[r],mh )
        return a
            


            
            