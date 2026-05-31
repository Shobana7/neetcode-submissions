class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_end = res[-1][1]
            if intervals[i][0] <= prev_end:
                res[-1][1] =  max(intervals[i][1], prev_end)
            else:
                res.append(intervals[i])
        
        return res
