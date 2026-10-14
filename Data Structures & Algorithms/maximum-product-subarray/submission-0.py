class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cur_min = cur_max = res = nums[0]
    
        for i in range(1, n):
            pre_max, pre_min = cur_max, cur_min
            cur_max = max(nums[i], pre_max * nums[i], pre_min * nums[i])
            cur_min = min(nums[i], pre_max * nums[i], pre_min * nums[i])
            if cur_max > res:
                res = cur_max
        
        return res



        