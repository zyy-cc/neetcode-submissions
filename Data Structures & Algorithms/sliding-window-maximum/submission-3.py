# from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        left = right = 0
        res = []
        q = deque()

        while right < len(nums):
            # if the new element is larger than the past element, we need to delete the small one. 
            # because it means the smaller one can't be the maximum value in the window
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)
            # store idx is to check if the index is still in this window or not
            if q[0] < left:
                q.popleft()
            
            if right >= k-1:
                res.append(nums[q[0]])

            if right - left + 1 >= k:
                left += 1
            right += 1
        return res


        
