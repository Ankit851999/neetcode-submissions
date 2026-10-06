class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len( prices) < 2:
            return 0
        p = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            mini = min(prices[i], mini)
            p = max(( prices[i] -mini), p)
        return p
            


