class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings = [[0,0]] + sorted(meetings) + [[days+1, days+1]]
        i = 0
        openDays = 0
        while i < len(meetings) and len(meetings) > i + 1:
            if meetings[i][1] >= meetings[i+1][0] -1:
                if meetings[i+1][1] > meetings[i][1]:
                    meetings[i][1] = meetings[i+1][1]
                meetings.pop(i+1)
            else:
                openDays += meetings[i+1][0] - meetings[i][1] - 1
                i += 1
        return openDays
