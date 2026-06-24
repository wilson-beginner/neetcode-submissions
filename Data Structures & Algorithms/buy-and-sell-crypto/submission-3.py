class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx = 0
        minPointer, bestProfit = 0, 0
        while idx < len(prices):
            if(prices[idx] < prices[minPointer]):
                minPointer = idx
            bestProfit = max(bestProfit, prices[idx]-prices[minPointer])
            idx += 1
        return bestProfit
             