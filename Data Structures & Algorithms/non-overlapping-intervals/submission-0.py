class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_interval = 0

        intervals.sort(key = lambda x: x[1])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start >= prev_end:
                # non-overlapping
                prev_end = cur_end
            else:
                # remove overlapping
                min_interval += 1
        return min_interval



        
        