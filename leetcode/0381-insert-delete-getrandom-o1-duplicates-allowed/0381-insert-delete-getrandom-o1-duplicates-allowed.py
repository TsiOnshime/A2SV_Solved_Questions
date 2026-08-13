class RandomizedCollection:

    def __init__(self):
        self.hashset = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.hashset:
            self.hashset[val] = {len(self.nums)}
            self.nums.append(val)
            return True
        self.hashset[val].add(len(self.nums))
        self.nums.append(val)
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashset:
            return False
        last_elem = self.nums[-1]
        for i in self.hashset[val]:
            idx = i
            break
            
        last_idx = len(self.nums) - 1
        self.hashset[last_elem].remove(last_idx)
        if idx != last_idx:
            self.hashset[val].remove(idx)
            self.hashset[last_elem].add(idx)
            self.nums[idx], self.nums[last_idx] = self.nums[last_idx], self.nums[idx]
        self.nums.pop()
        
        if len(self.hashset[val]) == 0:
            del self.hashset[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna