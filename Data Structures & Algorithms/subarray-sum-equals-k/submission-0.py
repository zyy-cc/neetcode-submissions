class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        # no sliding window because the element may be negative
        dic = {}
        dic[0] = 1
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum +=  nums[i]
            need = prefix_sum - k
            if need in dic:
                count += dic.get(need,0)
            dic[prefix_sum] = dic.get(prefix_sum, 0) + 1
        return count
    


        