class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right =0
        l = 0
        temp_k = k

        while right < len(s):

            while right + 1 < len(s) and s[left] == s[right +1 ]:
                right += 1
            temp_r = right
            temp_l = left

            while temp_r < len(s) -1 and temp_k != 0:
                temp_r += 1
                if s[temp_r] != s[left]:
                    temp_k -= 1
            
            while temp_l > 0 and temp_k != 0:
                temp_l -= 1
                if s[temp_l] != s[left]:
                    temp_k -= 1
            while temp_r + 1 < len(s) and s[temp_r + 1] == s[left]:
                temp_r += 1
            while temp_l - 1 < -1 and s[temp_l - 1] == s[left]:
                temp_l -= 1
            
            l = max(l, temp_r - temp_l + 1)

            right += 1
            left = right
            temp_k = k
        return l

            


                