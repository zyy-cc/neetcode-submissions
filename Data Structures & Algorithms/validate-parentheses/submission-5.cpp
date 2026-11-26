class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0) {
            return false;
        }

        stack<char> stk;
        unordered_map<char, char> mp = {
            {'}', '{'},
            {')', '('},
            {']', '['}
        };

        for (char c: s) {
            if (mp.count(c)) {
                if (stk.empty() || stk.top() != mp[c]) {
                    return false;
                }
                stk.pop();
            } else {
                stk.push(c);
            }
        }

        return stk.empty();
 
    }
};
