class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        dp = {}

        def dfs(i, holding):
            if i >= n:
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            if holding:
                # sell
                profit = max(dfs(i+1, holding), prices[i] + dfs(i + 2, False))
            else:
                # buy
                profit = max(dfs(i+1, holding), -prices[i] + dfs(i + 1, True))
            
            dp[(i, holding)] = profit
            return profit
        return dfs(0, False)
          