"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_interval = sorted(intervals, key= lambda x:x.start)
        prev_end, cur_start = -1, 0 
        for interval in sorted_interval:
            cur_start = interval.start
            if cur_start < prev_end:
                return False
            prev_end = interval.end
        return True
