class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)-1, -1, -1):
            seen[nums[i]] = i
        
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in seen:
                if seen[rest] != i:
                    return [min(i, seen[rest]), max(i, seen[rest])] 



        
        