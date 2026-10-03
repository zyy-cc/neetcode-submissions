class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # choose[0], don't consider n- 1
        def dfs(chosen):
            n = len(chosen)
            dp = [0 for _ in range(n+2)]
        
            for i in range(n-1, -1, -1):
                dp[i] = max(chosen[i] + dp[i+2], dp[i+1])
            return dp[0]
        first = dfs(nums[:-1])
        last = dfs(nums[1:])
        return max(first, last)




        