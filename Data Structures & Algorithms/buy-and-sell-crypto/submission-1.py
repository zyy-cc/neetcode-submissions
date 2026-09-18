class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0

        res = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(res, profit)
        
            right += 1
        return res
        