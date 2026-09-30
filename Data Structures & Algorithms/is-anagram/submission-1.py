class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maap = {}
        for i in range(len(s)):
            maap[s[i]] = maap.get(s[i], 0) + 1 
            maap[t[i]] = maap.get(t[i], 0) - 1 
        for i in maap:
            if maap[i] != 0:
                return False
        return True


        
