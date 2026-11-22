class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = float("-inf")
        max_sum = float("-inf")
        
        for i in range(len(nums)):
            # either we start with the new element, or we add this number
            cur_sum = max(cur_sum + nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum


        
        