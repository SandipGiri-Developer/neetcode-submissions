class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Max = 0
        buy = prices[0]
        for i in prices[1:]:
            if i < buy:
                buy = i
            Max = max(Max,i-buy)
        return Max    
        