class RandomizedSet:

    def __init__(self):
        self.sett = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.sett:
            return False

        idx = len(self.arr)

        self.sett[val] = idx
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.sett:
            return False
        
        idx = self.sett[val]
        # when we are told to delete an element at 2, we swap it with the last element so it would be an O(1) for array
        # [2, 3, 1, 6] val = 3          {2: 0, 3: 1, 1: 2, 6: 3}
        # [2, 6, 1, 3] then pop()       {2: 0, 6: 1, 1: 2}
        last_elem = self.arr[-1]
        self.sett[last_elem] = idx

        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr.pop()
        del self.sett[val]
        return True
        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna