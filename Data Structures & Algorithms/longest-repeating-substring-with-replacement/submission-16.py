class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        n = len(s)
        if n == 0:
            return 0
        left = 0
        ans = 0
        for right in range(n):
            count[ord(s[right]) - ord("A")] += 1

            while( right -left +1 ) -max(count) >k:
                count[ord(s[left]) - ord("A")] -= 1
                left += 1
            
            ans = max(ans , right -left +1)
        return ans