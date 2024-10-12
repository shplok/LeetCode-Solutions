class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # min # groups needed == max # intervals that overlap at some point
        events = []
        for interval in intervals:
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))

        events.sort(key=lambda x: (x[0], x[1]))
        concurrentIntervals = 0
        maxConcurrentIntervals = 0

        for event in events:
            concurrentIntervals += event[1]
            maxConcurrentIntervals = max(concurrentIntervals, maxConcurrentIntervals)

        return maxConcurrentIntervals