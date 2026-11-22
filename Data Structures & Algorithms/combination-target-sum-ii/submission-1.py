class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # avoid repetition
        candidates.sort()
        path = []
        res = []
        cur_sum = 0

        def backtrack(start):
            nonlocal cur_sum
            # return condition
            if cur_sum == target:
                res.append(path[:])
                return 
            elif cur_sum > target:
                return 
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                cur_sum += candidates[i]
                backtrack(i + 1)
                path.pop()
                cur_sum -= candidates[i]
        backtrack(0)
        return res

        