class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # length 1, length 2, length 3, dp[i][j] = string[i:j+1] is palindromic or not
        dp = [[False] * n for _ in range(n)]
        max_len = 0
        start = 0

        # length of a string
        for l in range(1, n + 1):
            # starting index
            for i in range(n - l + 1):
                j = i + l - 1
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                
                if dp[i][j] == True:
                    if l > max_len:
                        max_len = l
                        start = i
        return s[start: start + max_len]
                



        