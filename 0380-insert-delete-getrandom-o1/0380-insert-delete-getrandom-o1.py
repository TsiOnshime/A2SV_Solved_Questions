class RandomizedSet:

    def __init__(self):
        self.num_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.num_idx:
            self.num_idx[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.num_idx:
            return False
        curr_idx = self.num_idx[val]
        last_elem = self.nums[-1]
        self.num_idx[last_elem] = curr_idx
        self.nums[-1], self.nums[curr_idx] = self.nums[curr_idx], self.nums[-1]
        self.nums.pop()
        del self.num_idx[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna