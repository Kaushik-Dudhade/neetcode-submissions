class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        largest = prices[-1]

        for i in prices[::-1]:
            if i < largest:
                profit = max(profit, largest - i)
            
            else:
                largest = i
        
        return profit