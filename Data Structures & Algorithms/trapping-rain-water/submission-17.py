class Solution: 
    def trap(self, height):
        n = len(height)
        if n <3:
            return 0
        l =0
        r = n-1
        ml = 0
        mr = 0
        mh = 0
        a = 0

        while r>l:
            if height[l] > height[r]:
                a += (mr - min(mr,height[r]))
                mr = max(mr,height[r] )
                r -= 1
            else:
                a +=( ml -min(ml,height[l]))
                ml = max(ml,height[l] )
                l += 1
        return a

            


            
            