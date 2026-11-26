class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}
        def dfs(i, cur_sum):
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]
            # base case
            if i == len(nums):
                if cur_sum == target:
                    return 1
                else:
                    return 0
            
            memo[(i, cur_sum)] = dfs(i+1, cur_sum + nums[i]) + dfs(i + 1, cur_sum - nums[i])
            return memo[(i, cur_sum)]
        return dfs(0,0)

        
            

            

        