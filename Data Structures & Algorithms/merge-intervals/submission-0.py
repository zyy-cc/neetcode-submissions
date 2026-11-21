class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start
        intervals.sort(key = lambda x: x[0])
        res = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= end:
                # merge
                end = max(end, cur_end)
            else:
                # only when non-overlapping
                res.append([start, end])
                start = cur_start
                end = cur_end
        res.append([start, end])
        return res
            



        