class Solution: 
    def trap(self, height):
        n = len(height)
        if n <3:
            return 0
        l =0
        r = n-1
        ml = 0
        mr = 0
        a = 0

        while r>l:
            if height[l] > height[r]:
                mr = max(mr,height[r] )
                a += (mr - height[r])
                r -= 1
            else:
                ml = max(ml,height[l] )
                a +=( ml-  height[l])
                l += 1
        return a

            


            
            