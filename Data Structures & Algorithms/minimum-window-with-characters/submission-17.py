class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = [0] * 80
        maap = {}
        a = ord("a")
        if len(t) > len(s):
            return ""
        
        # t_count = {}
        s_indexs = {}

        def getcounts(left):
            extra = 0
            less = 0
            left_count = t_count[ord(s[left]) - a]
            for i in t_count:
                if i >0:
                    less += 1
                elif i < 0:
                    extra += 1
            return extra, less, left_count

        for i in range(len(t)):
            t_count[ord(t[i])-a] += 1
            maap[t[i]] = maap.get(t[i], 0) +1
        
        smallest_len = 0
        indexes = []
        
        left = None
        right = 0

        for right in range(len(s)):
            if s[right] in maap:
                i = ord(s[right]) - a
                t_count[i] -= 1

                if left == None:
                    left = right

                extra, less, left_count = getcounts(left)


            
                while left_count <= 0 and less == 0:
                    if s[left] in maap:
                        extra, less, left_count = getcounts(left)
                        if left_count == 0:
                            break
                        t_count[ord(s[left]) - a] += 1
                    left += 1


                if less == 0 and (smallest_len == 0 or smallest_len > right - left + 1):
                    indexes = [left, right]
                    smallest_len =  right - left + 1
        if len(indexes) == 0:
            return ""
        else:
            return s[indexes[0]: indexes[1]+1]