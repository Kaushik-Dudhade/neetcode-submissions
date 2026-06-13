class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <=1:
            return 0

        profit = 0
        smallest_seen = prices[0]

        for i in prices[1:]:
            if i > smallest_seen:
                profit = max(profit, i - smallest_seen)
            
            elif i < smallest_seen:
                smallest_seen = i
                continue
        
        return profit


        