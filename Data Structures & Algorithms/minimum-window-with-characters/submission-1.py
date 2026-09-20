class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        

        t_dict = {}
        for ele in t:
            t_dict[ele] = t_dict.get(ele, 0) + 1
        
        left = right = 0
        best_left = 0
        best_len = len(s) + 1
        window = {}

        def valid(window, t_dict):
            for key in t_dict.keys():
                if window.get(key,0) < t_dict[key]:
                    return False
            return True

        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1
            
            while valid(window, t_dict):
                if right - left + 1 < best_len:
                    best_left = left 
                    best_len = right - left + 1

                if window[s[left]] > 1:
                    window[s[left]] -= 1
                else:
                    del window[s[left]]
                left += 1
            
            right += 1
        
        if best_len == len(s) + 1:
            return ""
        else:
            return s[best_left:best_left + best_len]
        
        