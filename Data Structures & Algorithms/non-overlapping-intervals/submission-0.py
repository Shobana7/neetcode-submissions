class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        intervals.sort()
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                count += 1
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
            else:
                prev = intervals[i]

        return count
        
