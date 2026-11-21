class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = set()
        ans = 0
        while right < len(s):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            ans = max(ans, len(window))
            right += 1
        return ans
        
        

        