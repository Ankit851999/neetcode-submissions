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
        # for i in range(1,n):
        #     if arr[i-1] == arr[i]:
        #         pre[i] = pre[i-1] + 1
        #     else:
        #         pre[i] = 1
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
            if i == 59:
                print(i)
            while right < n:
                if(arr[right] == arr[left]):
                    l = max(l, right - left +1)
                    if l == 6:
                        print(l)
                    right += 1
                else:
                    if post[right] > tempk:
                        break
                    else:
                        if 0 ==  tempk:
                            break
                        else:
                            tempk -= post[right]
                            right += post[right] 
                            l = max(l, right - left)

            right -= 1
            if tempk > 0:
                while left > -1:
                    if(arr[right] == arr[left]):
                        l = max(l, right - left +1)
                        if l == 6:
                            print(l)
                        left -= 1
                    else:
                        if 0 ==  tempk:
                            break
                        else:
                            tempk -= 1
                            left -= 1
                            l = max(l, right - left)
        return l