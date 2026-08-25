"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        min_rooms = 0

        timelines = []
        for interval in intervals:
            timelines.append((interval.start,1))
            timelines.append((interval.end,-1))
        
        timelines.sort()
        cur_rooms = 0
        for _, val in timelines:
            cur_rooms += val
            min_rooms = max(min_rooms, cur_rooms)
        
        return min_rooms 
            