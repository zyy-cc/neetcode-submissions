class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]
            # three cases
            # if the new interval is on the right
            if end < new_start:
                res.append([start, end])
            # if the new interval is on the left
            elif new_end < start:
                res.append([new_start, new_end])
                res.extend(intervals[i:])
                return res
            # if it is overlapping, update the new interval
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        res.append([new_start, new_end]) # in case, until the end, we didn't add this
        return res

        


        