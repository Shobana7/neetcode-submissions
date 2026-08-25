class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        to_be_removed = 0
        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                to_be_removed += 1
            else:
                prevEnd = intervals[i][1]

        return to_be_removed