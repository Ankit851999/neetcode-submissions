class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lisst = list(s)
        l = 0
        for i,val in enumerate(lisst):
            isduplicate = False
            j  = i + 1
            word = lisst[i]
            n = 1
            while isduplicate == False and j != len(lisst):
                if lisst[j] not in word:
                    word += lisst[j]
                    n += 1
                    j += 1
                else:
                    isduplicate = True
            l = max(l,n)
        return l

        