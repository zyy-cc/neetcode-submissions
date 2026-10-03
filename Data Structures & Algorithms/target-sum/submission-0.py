class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        dp = {}

        def dfs(i, cur_sum):
            if i == size:
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]

            cnt = dfs(i+1, cur_sum + nums[i]) + dfs(i+1, cur_sum - nums[i])
            dp[(i, cur_sum)] = cnt
            return cnt 
        return dfs(0,0)
        