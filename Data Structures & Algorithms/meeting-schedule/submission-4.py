"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)

        prevEnd = intervals[0].end
        i = 1

        while i < len(intervals):
            if prevEnd > intervals[i].start:
                return False
            prevEnd = intervals[i].end
            i += 1
        
        return True