from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.k = k
     

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.queue.append(num)
        else: 
            self.queue.clear()
        if len(self.queue) < self.k:
            return False
        while len(self.queue) > self.k:
            self.queue.popleft()
        return True




        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)