class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # first element is how many pass
        # second element are how many total
        
        def calc_gain(passes, total):
            return (passes+1) / (total+1) - passes / total

        max_heap = []
        for passes,total in classes:
            gain = calc_gain(passes,total)
            max_heap.append((-gain, passes, total))

        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            curr_gain, passes, total = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-calc_gain(passes+1,total+1),passes+1,total+1,),)

        pass_ratio = sum(passes / total for _, passes, total in max_heap)

        return pass_ratio / len(classes)
