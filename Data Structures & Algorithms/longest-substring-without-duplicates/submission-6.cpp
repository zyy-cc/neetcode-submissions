class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left = 0;
        int right = 0;
        unordered_set<char> seen;
        int res = 0;

        while (right < s.size()) {
            while (seen.count(s[right])) {
                seen.erase(s[left]);
                left ++;
            }
            seen.insert(s[right]);
            res = max(res, (int) seen.size());
            right ++;
        }  
        return res;   
    }
};
