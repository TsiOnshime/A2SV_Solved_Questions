class RecentCounter:

    def __init__(self):
        self.queue = []
        self.start = 0
       

    def ping(self, t: int) -> int:
        # interval = [t - 3000, t]
        # self.count = 0
        self.queue.append(t)
        while self.queue[-1] - self.queue[self.start] > 3000:
            self.start += 1
        return len(self.queue) - self.start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)