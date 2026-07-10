class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a,b = b,a
        
        l = 0
        r = len(a)
        total = len(a) + len(b)
        half =( total +1 )//2
        while l<= r:
            i = (l+r) //2
            j = half - i

            aleft = a[i-1] if i > 0 else float("-inf")
            aright = a[i] if i < len(a) else float("inf")

            bleft = b[j-1] if j > 0 else float("-inf")
            bright = b[j] if j < len(b) else float("inf")

            if aleft <= bright and bleft <= aright:
                if total % 2 :
                    return max(aleft, bleft)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1
