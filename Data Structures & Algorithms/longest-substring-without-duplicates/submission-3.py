class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lisst = list(s)
        l = 0
        indexes = {}
        left, right = 0,0
        for i,val in enumerate(lisst):
            if val in indexes:
                if indexes[val][-1] + 1 > left:
                    left = indexes[val][-1] + 1
                indexes[val].append(i)
            else:
                indexes[val] = [i]
            right = i
            l = max(right - left +1, l)        
        return l