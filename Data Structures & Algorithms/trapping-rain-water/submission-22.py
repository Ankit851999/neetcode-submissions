class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        l = 0
        r = len(h) -1
        if r <= 1:
            return 0
        area = 0
        last_min_h = 0
        while l < r:
            area +=  (min(
                h[l] - last_min_h,
                h[r] - last_min_h
                ) * (r-l-1)) -last_min_h
            if h[l] > h[r]:
                last_min_h = h[r]
                while (
                    last_min_h >= h[r-1] and r-1 > l
                    ):
                    r -= 1
                    area -= h[r]
                r -= 1
            else:
                last_min_h = h[l]
                while (
                    last_min_h >= h[l+1] and l+1 < r
                    ):
                    l += 1
                    area -= h[l]
                l += 1
        return area
