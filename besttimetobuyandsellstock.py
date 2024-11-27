class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        
        lowest = float('inf')
        max_profit = 0

        for price in prices:
            if price < lowest:
                lowest = price
            
            profit = price - lowest
            if profit > max_profit:
                max_profit = profit 
                
        return max_profit