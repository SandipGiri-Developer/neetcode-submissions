class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        n = len(prices)
        for i in range(n):
            for j in range(i,n):
                Max = max(Max,prices[j] - prices[i])

        return Max
        