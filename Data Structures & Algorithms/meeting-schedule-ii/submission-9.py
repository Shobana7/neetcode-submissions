"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        timelines = []
        for i in intervals:
            timelines.append((i.start, 1))
            timelines.append((i.end,-1))
        timelines.sort()
        maxRooms = 0
        curRooms = 0
        for _, val in timelines:
            curRooms += val
            maxRooms = max(maxRooms, curRooms)
        
        return maxRooms
