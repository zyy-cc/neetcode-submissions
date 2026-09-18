class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        long_res = 0
        window = set()

        while right < len(s):
            while s[right] in window:
                window.discard(s[left])
                left += 1
            window.add(s[right])
            long_res = max(long_res, len(window))
            right += 1

        return long_res
        

        