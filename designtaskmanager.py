class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.heap = []
        self.tPriority = {}
        self.owner = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.tPriority[taskId] = priority
        self.owner[taskId] = userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.tPriority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.tPriority[taskId] = -1

    def execTop(self) -> int:
        while self.heap:
            negp, negid = heapq.heappop(self.heap)
            p = -negp
            tid = -negid
            if self.tPriority.get(tid, -2) == p:
                self.tPriority[tid] = -1
                return self.owner.get(tid, -1)
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
