class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_dict = {}
        for ele in t:
            t_dict[ele] = t_dict.get(ele, 0) + 1
        

        window = {}
        need = len(t_dict)
        have = 0

        left = right = 0
        best_len = len(s) + 1
        best_left = 0



        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in t_dict and window[s[right]] == t_dict[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                if s[left] in t_dict and window[s[left]] == t_dict[s[left]]:
                    have -= 1

                if window[s[left]] > 1:
                    window[s[left]] -= 1
                else:
                    del window[s[left]]
                
                

                left += 1
            
            right += 1
        if best_len == len(s) + 1:
            return ""
        else:
            return s[best_left: best_left + best_len]





            
        
        