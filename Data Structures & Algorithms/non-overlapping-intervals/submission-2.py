class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        minCount = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                minCount += 1
            else:
                prevEnd = intervals[i][1]
        
        return minCount


