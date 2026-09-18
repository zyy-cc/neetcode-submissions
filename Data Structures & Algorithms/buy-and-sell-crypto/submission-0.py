class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = right = 0

        res = 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            while prices[right] < prices[left]:
                left += 1
            res = max(res, profit)
            right += 1
        return res
        