class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seen_s, seen_t = {}, {}
        for i in range(len(s)):
            seen_s[s[i]] = seen_s.get(s[i], 0)+ 1
            seen_t[t[i]] = seen_t.get(t[i], 0)+ 1
        
        for key, val in seen_s.items():
            if not (key in seen_t):
                return False
            elif val != seen_t[key]:
                return False
        return True
            

      
        