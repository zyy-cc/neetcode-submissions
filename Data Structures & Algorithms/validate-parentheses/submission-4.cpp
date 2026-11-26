class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0){
            return false;
        }

        unordered_map<char, char> mp = {{')','('}, {'}','{'}, {']','['}};
        stack<char> st;

        for (char c: s) {
            if (mp.count(c)) {
                if (st.empty() ||  mp[c] != st.top()) {
                    return false;
                }
                st.pop();
            } else {
                st.push(c);
            }
        }

        return st.empty();
        
    }
};
