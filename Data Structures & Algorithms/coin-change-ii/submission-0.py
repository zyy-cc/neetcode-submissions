class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        def dfs(i, cur_left):
            if cur_left == 0:
                return 1

            if i == n or cur_left < 0:
                return 0

            if (i, cur_left) in dp:
                return dp[(i, cur_left)]    

            dp[(i, cur_left)] = dfs(i+1, cur_left) + dfs(i, cur_left - coins[i])
            return dp[(i, cur_left)]

        return dfs(0, amount)
        