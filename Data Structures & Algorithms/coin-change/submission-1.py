class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(i, cur_left):
            if cur_left == 0:
                return 0
            elif i == len(coins) or cur_left < 0:
                return float("inf")
            
            if (i, cur_left) in memo:
                return memo[(i, cur_left)]
            
            res= min(dfs(i + 1, cur_left), dfs(i, cur_left - coins[i]) + 1)
            memo[(i, cur_left)] = res
            return res
        res = dfs(0, amount)
        return -1 if res == float("inf") else res


        