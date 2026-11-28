class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        // order by start time
        sort(intervals.begin(), intervals.end());

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (auto& interval: intervals) {
            int new_start = interval[0];
            int new_end = interval[1];

            if (new_start <= end) {
                // merge
                end = max(new_end, end);
            } else {
                // non-overlapping
                res.push_back({start, end});
                start = new_start;
                end = new_end;
            }
        }

        res.push_back({start, end});
        return res;
        
    }
};
