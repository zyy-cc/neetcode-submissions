class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # we only need to keep the current furthest
        furthest = 0

        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
        return True