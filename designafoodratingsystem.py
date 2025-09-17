from collections import defaultdict
from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodRMap = {} 
        self.foodCMap = {} 
        self.cuisineMap = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.foodRMap[foods[i]] = ratings[i]
            self.foodCMap[foods[i]] = cuisines[i]
            self.cuisineMap[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine_name = self.foodCMap[food]
        old = (-self.foodRMap[food], food)
        self.cuisineMap[cuisine_name].remove(old)
        self.foodRMap[food] = newRating
        self.cuisineMap[cuisine_name].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest = self.cuisineMap[cuisine][0]
        return highest[1]
