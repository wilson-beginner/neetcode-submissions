class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        minPointer, maxPrice, bestProfit = 0, 0, 0
        for idx in range(1, len(prices)):
            if(idx < len(prices)-1 and prices[idx] < prices[minPointer]):
                minPointer = idx
                maxPrice = 0
            if(prices[idx]>maxPrice):
                maxPrice = prices[idx]
                bestProfit = max(bestProfit, maxPrice-prices[minPointer])
        return bestProfit
             