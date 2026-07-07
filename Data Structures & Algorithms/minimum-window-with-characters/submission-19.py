class Solution:
    def minWindow(self, s: str, t: str) -> str:
        maap = {}
        a = ord("a")
        if len(t) > len(s):
            return ""

        for i in range(len(t)):
            maap[t[i]] = maap.get(t[i], 0) +1
        
        smallest_len = 0
        indexes = []
        
        left = None
        right = 0

        required = len(t)

        for right in range(len(s)):
            if s[right] in maap:
                maap[s[right]] -= 1
                if maap[s[right]] >= 0:
                    required -= 1
                if left == None:
                    left = right
            
                while (maap.get(s[left], -1) < 0) and required == 0:
                    if s[left] in maap:
                        maap[s[left]] += 1
                    left += 1

                if required == 0 and (smallest_len == 0 or smallest_len > right - left + 1):
                    indexes = [left, right]
                    smallest_len =  right - left + 1
        if len(indexes) == 0:
            return ""
        else:
            return s[indexes[0]: indexes[1]+1]