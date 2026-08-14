class TimeMap:

    def __init__(self):
        self.timeStamp = defaultdict(list)

    def binarySearch(self, l, r, key, timestamp):
        ans = ""
        while l <= r:
            mid = l + (r - l)//2
            if self.timeStamp[key][mid][1] > timestamp:
                r = mid - 1
            else:
                ans = self.timeStamp[key][mid][0]
                l = mid + 1
        return ans

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStamp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.timeStamp[key]) == 0:
            return ""
        l = 0
        r = len(self.timeStamp[key]) - 1
        return self.binarySearch(l, r, key, timestamp)
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna