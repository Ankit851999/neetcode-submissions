class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = {}
        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
        left = 0
        for right in range(len(s2)):
            if s2[right] in count:
                count[s2[right]] -= 1
            if (right - left +1) > len(s1):
                if s2[left] in count:
                    count[s2[left]] += 1
                left += 1
            isPur = True
            for key, val in count.items():
                if val != 0:
                    isPur = False
                    break
            if isPur:
                return True

        return False