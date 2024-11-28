class RandomizedSet:

    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        else:
            self.data.append(val)
            self.index_map[val] = len(self.data) - 1
            return True
            
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        else:
            temp = self.data[-1]
            index_remove = self.index_map[val]

            self.data[index_remove] = temp
            self.index_map[temp] = index_remove

            self.data.pop()
            del self.index_map[val]
            return True
        
    def getRandom(self) -> int:
        return random.choice(self.data)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()