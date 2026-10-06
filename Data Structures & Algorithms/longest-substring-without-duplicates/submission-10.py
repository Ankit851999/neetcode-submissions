class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        left = 0
        right = 0
        obj = {}
        while right < len(s):
            if s[right] in obj:
                while left < len(s) and s[left] != s[right]:
                    del obj[s[left]]
                    left += 1
                del obj[s[left]]
                obj[s[right]] = right
                left += 1
                right +=1

            else:
                obj[s[right]] = right
                l = max(l, right-left+1)
                right += 1

        return l