class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = {}
        for s in s1:
            s1_dict[s] = s1_dict.get(s, 0) + 1
        
        left = right = 0
        s2_dict = {}

        while right < len(s2):
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1
            
            while (right - left + 1) > len(s1):    
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] <= 0:
                    del s2_dict[s2[left]]
                left += 1
            
            if s1_dict == s2_dict:
                return True
            right += 1

        return False
        