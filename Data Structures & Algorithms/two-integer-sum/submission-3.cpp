class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            auto it = mp.find(diff); // return a iterator

            if (it != mp.end()) {
                return {it->second, i};
            }
            mp[nums[i]] = i;
        }
    }
};
