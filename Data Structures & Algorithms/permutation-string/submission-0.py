class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        for right in range(len(s1)-1,len(s2)):
            temp = list(s1)
            left = right -len(s1) +1
            isPur = True
            for i in range(left,right+1):
                if s2[i] in temp:
                    temp.remove(s2[i])
            if not len(temp):
                return True
        return False
            
            