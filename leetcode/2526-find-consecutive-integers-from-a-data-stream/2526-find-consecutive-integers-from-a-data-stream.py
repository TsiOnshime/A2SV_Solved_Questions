from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.timeseen = 0
     

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.timeseen += 1
            if self.timeseen >= self.k:
                return True
        else:
            self.timeseen = 0

        return False



        

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)