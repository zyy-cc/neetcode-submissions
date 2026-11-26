class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            if new_start > end:
                res.append([start, end])
                continue
            elif new_end < start:
                res.append([new_start, new_end])
                res.extend(intervals[i:])
                return res
            else:
                # merge
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        res.append([new_start, new_end])
        return res
            
            



        