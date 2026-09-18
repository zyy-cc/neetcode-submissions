class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        ans = 0

        window = {}

        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1

            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

            right += 1

        return ans
        