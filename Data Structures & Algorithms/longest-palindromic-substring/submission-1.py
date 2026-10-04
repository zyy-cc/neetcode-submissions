class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd
            l, r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res
        # n = len(s)
        # # length 1, length 2, length 3, dp[i][j] = string[i:j+1] is palindromic or not
        # dp = [[False] * n for _ in range(n)]
        # max_len = 0
        # start = 0

        # # length of a string
        # for l in range(1, n + 1):
        #     # starting index
        #     for i in range(n - l + 1):
        #         j = i + l - 1
        #         if l == 1:
        #             dp[i][j] = True
        #         elif l == 2:
        #             dp[i][j] = s[i] == s[j]
        #         else:
        #             dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
        #         if dp[i][j] == True:
        #             if l > max_len:
        #                 max_len = l
        #                 start = i
        # return s[start: start + max_len]
                



        