class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            res = 0
            # s[i:] the number of ways to decode it
            # base case 1
            if i == n:
                return 1
            
            # a decoding cannot start with "0"
            if s[i] == "0":
                return 0
                
            # use one digit 
            res += dfs(i+1)
            if i + 1 < n and int(s[i:i+2]) < 27:
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)



        