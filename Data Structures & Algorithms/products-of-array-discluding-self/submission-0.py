class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [1] * n, [1] * n
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        return [prefix[i] * suffix[i] for i in range(n)]
        


        