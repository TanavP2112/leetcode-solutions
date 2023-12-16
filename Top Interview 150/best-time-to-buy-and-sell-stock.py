class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        profit = 0
        while end < len(prices):
            if prices[end] > prices[start]:
                profit = max(profit, prices[end] - prices[start])
            else:
                start = end
            end += 1
        return profit