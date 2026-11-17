class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        requirement = len(nums) // 3
        res = []
        for ele in nums:
            count[ele] = count.get(ele, 0) + 1

        for key, val in count.items():
            if val > requirement:
                res.append(key)
        return res



        