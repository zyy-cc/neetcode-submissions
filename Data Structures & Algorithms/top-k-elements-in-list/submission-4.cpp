class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num] ++;
        }
        vector<pair<int, int>> v;
        for (auto& [num, count]: freq) {
            v.push_back({count, num});
        }
        sort(v.begin(), v.end(), greater<pair<int, int>>());
        vector<int> res;
        for (int i = 0; i < k; i++) {
            res.push_back(v[i].second);
        }
        return res;
         
    }
};
