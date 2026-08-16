class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 1
        result = [intervals[0]]
        while i < len(intervals):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
            i += 1
        
        return result
