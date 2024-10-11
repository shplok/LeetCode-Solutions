class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        targetArrival = times[targetFriend][0]
        times = sorted(
            [(arrival, leave, index) for index, (arrival, leave) in enumerate(times)]
        )

        leaving = []
        nextChair = 0
        availableChairs = set()

        for arrival, leave, index in times:
            while leaving and leaving[0][0] <= arrival:
                _, freedChair = heappop(leaving)
                availableChairs.add(freedChair)
            if availableChairs:
                assigned = min(availableChairs)
                availableChairs.remove(assigned)
            else:
                assigned = nextChair
                nextChair += 1
            if index == targetFriend:
                return assigned

            heappush(leaving, (leave, assigned))
