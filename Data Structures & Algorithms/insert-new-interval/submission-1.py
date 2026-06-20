class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        res = []
        merged = newInterval.copy()
        pos = 0

        for interval in intervals:
            if ((interval[0] <= merged[0] <= interval[1] or interval[0] <= merged[1] <= interval[1]) or 
                (merged[0] <= interval[0] <= merged[1] or merged[0] <= interval[1] <= merged[1])):
                temp = merged.copy()
                merged[0] = interval[0] if interval[0] < temp[0] else temp[0]
                merged[1] = interval[1] if interval[1] > temp[1] else temp[1]
                continue
            res.append(interval)

        res.append(merged)
        return sorted(res)



