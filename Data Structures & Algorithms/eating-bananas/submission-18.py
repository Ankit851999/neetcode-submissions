class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minimumRate = piles[0]
        maximumRate = piles[0]
        import math
        total = 0
        for i in piles:
            if i < minimumRate:
                minimumRate = i
            elif i > maximumRate:
                maximumRate = i
            total += i
        if len(piles) == h:
            return maximumRate
        left = 1
        right = maximumRate 
        arr = []
        while left <= right:
            mid = (left + right) //2
            hrs = 0
            for i in piles:
                hrs += math.ceil(i/mid)
            if hrs <= h:
                arr.append([hrs, mid])
            if hrs <= h:
                right = mid -1
            else:
                left = mid + 1
                
        maxAns = []
        print(arr)
        for i in range(len(arr)-1, -1,-1):
            if not maxAns:
                maxAns = arr[i]
            elif maxAns[0] <= arr[i][0] and maxAns[1] > arr[i][1]:
                maxAns = arr[i]
        return maxAns[1]