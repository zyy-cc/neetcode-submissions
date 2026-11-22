class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        cur_sum = 0

        def backtrack(start):
            nonlocal cur_sum
            if cur_sum == target:
                res.append(path[:])
                return 
            elif cur_sum > target:
                return 
            for i in range(start, len(nums)):
                cur_sum += nums[i]
                path.append(nums[i])
                backtrack(i)
                path.pop()
                cur_sum -= nums[i]
        backtrack(0)
        return res

        