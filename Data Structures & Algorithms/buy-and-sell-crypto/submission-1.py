class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        right = 1
        left = 0
        p = 0
        while right < n:
            if prices[right] > prices[left]:
                p = max(p, prices[right]- prices[left])
                if right +1 == n:
                    return p 
                if prices[right +1] < prices[left]:
                    left = right +1
                    right = left +1
                else :
                    right += 1
            else:
                left = right
                right = left +1
        return p