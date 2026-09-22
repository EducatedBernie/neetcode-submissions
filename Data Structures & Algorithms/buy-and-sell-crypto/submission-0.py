class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        buyDay = 0
        sellDay = 1
        
        maxProf = float("-inf")

        while sellDay != len(prices): # sellDay = len 
            if prices[sellDay] < prices[buyDay]:
                buyDay = sellDay #buyDay now 1 
            # oldProf = maxProf
            maxProf = max(maxProf, prices[sellDay] - prices[buyDay])
            sellDay += 1 # #sellDay now 2
        
        if maxProf < 0:
            return 0
        return maxProf