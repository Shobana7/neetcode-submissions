"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:x.start)
        heap = [intervals[0].end]
        days = 1
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            else:
                days += 1
            heapq.heappush(heap, intervals[i].end)
        
        return days 