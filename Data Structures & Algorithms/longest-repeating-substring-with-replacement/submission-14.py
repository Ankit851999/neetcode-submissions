class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        arr = list(s)
        n = len(arr)
        if n == 0:
            return 0
        l = 1
        pre = [0] * n
        pre[0] = 1
        post = [0] * n
        post[n-1] = 1
        for i in range(n-2,-1,-1):
            if arr[i+1] == arr[i]:
                post[i] = post[i+1] +1
            else:
                post[i] = 1
        for i in range(n):
            if(i > 0 and arr[i] == arr[i-1]):
                continue
            right = i +1
            left = i
            tempk = k
            if right == n:
                l = max(l,1)
                continue
            while right < n:
                if arr[left] == arr[right]:
                    right += 1
                    l = max(l, right -left)
                else:
                    if tempk == 0:
                        break
                    tempk -= 1
                    right += 1
                    l = max(l , right -left)
            if right == n:
                right -= 1
            if tempk > 0:
                while left > -1:
                    if arr[left] == arr[right]:
                        left -= 1
                        l = max(l, right - left)
                    else:
                        if tempk == 0:
                            break
                        tempk -= 1
                        left -= 1
                        l = max(l , right -left)
        return l