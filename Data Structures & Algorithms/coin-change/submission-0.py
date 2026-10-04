class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = {}
        
        def dfs(i, cur_left):
            if cur_left == 0:
                return 0
            if i == n or cur_left < 0:
                # this should be impossible case
                return float("inf")

            if (i, cur_left) in dp:
                return dp[(i, cur_left)]

            dp[(i, cur_left)] = min(dfs(i+1, cur_left), dfs(i, cur_left - coins[i]) + 1)
            return dp[(i, cur_left)]

        res = dfs(0, amount)

        return -1 if res == float("inf") else res

            
        