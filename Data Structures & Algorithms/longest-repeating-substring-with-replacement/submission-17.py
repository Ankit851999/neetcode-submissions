class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        n = len(s)
        if n == 0:
            return 0
        left = 0
        ans = 0
        maxfreq = 0
        for right in range(n):
            count[s[right]] = count.get(s[right], 0) + 1
            maxfreq = max(maxfreq, count[s[right]])
            while( right -left +1 ) - maxfreq >k:
                count[(s[left])] -= 1
                left += 1
            
            ans = max(ans , right -left +1)
        return ans