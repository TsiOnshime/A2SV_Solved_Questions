class RandomizedSet:

    def __init__(self):
        self.map = defaultdict(int)
        self.list = []

    def insert(self, val: int) -> bool:

        if val in self.map:
            return False

        self.list.append(val)
        self.map[val] = len(self.list) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        curr_val_index = self.map[val]


        last_idx = len(self.list) - 1

        self.map[self.list[last_idx]] = curr_val_index

        self.list[curr_val_index], self.list[last_idx] = self.list[last_idx], self.list[curr_val_index]

        self.list.pop()
        del self.map[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()