class UndergroundSystem:

    def __init__(self):
        self.arrivals = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.arrivals[id] = [id, stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        duration = t - self.arrivals[id][2]
        start = self.arrivals[id][1]
        if (start, stationName) not in self.averages:
            self.averages[(start, stationName)] = [duration, 1]
        else:
            self.averages[(start, stationName)] = [duration + self.averages[(start, stationName)][0], self.averages[(start, stationName)][1] + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[(startStation, endStation)][0] / self.averages[(startStation, endStation)][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna