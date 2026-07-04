class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        leftmax = [0] * n
        rightmax = [0] * n
        leftmax[0] = prices[0]
        for i in range(1,n):
            leftmax[i] = min(leftmax[i-1], prices[i])

        rightmax[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], prices[i])
        maxprofit = 0
        for i in range(n):
            maxprofit = max(maxprofit, rightmax[i] -leftmax[i])
        return maxprofit
             