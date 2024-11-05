class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(key=lambda b: -b)
        count = 0

        for box in capacity:
            apples -= box
            count += 1
            if apples <= 0:
                return count
        return -1
