class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = [0] * 80
        a = ord("a")
        if len(t) > len(s):
            return ""

        for i in range(len(t)):
            t_count[ord(t[i]) - a] += 1
        
        minString = ""
        for left in range(len(s)):
            temp = t_count.copy()
            totol = len(t)
            li = ord(s[left]) - a
            right = left
            temp[li] -= 1

            if temp[li] >= 0:
                totol -= 1
            
            if totol == 0:
                minString = s[left:right+1]
                continue
            right += 1
            while right < len(s):
                ri = ord(s[right]) - a
                temp[ri] -= 1
                if temp[ri] >= 0:
                    totol -= 1

                is_sallest = False
                if minString == "":
                    is_sallest = True
                elif right -left + 1 < len(minString):
                    is_sallest = True
                if totol == 0 and is_sallest:
                    minString = s[left:right+1]
                    break
                right += 1
        return minString