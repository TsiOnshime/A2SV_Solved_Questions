class StockPrice:

    def __init__(self):
        self.timestamp_price = defaultdict(int)
        self.curr_time = 0
        self.min_heap = []
        self.max_heap = []
        

    def update(self, timestamp: int, price: int) -> None:
        
        self.timestamp_price[timestamp] = price
        self.curr_time = max(self.curr_time, timestamp)

        heapq.heappush(self.min_heap, [price, timestamp])
        heapq.heappush(self.max_heap, [-price, timestamp])

    def current(self) -> int:
        return self.timestamp_price[self.curr_time]
    def maximum(self) -> int:
        curr_price, timestamp = heapq.heappop(self.max_heap)

        while -curr_price != self.timestamp_price[timestamp]:
            curr_price, timestamp = heapq.heappop(self.max_heap)
        heapq.heappush(self.max_heap, [curr_price, timestamp])
        return -curr_price
        

    def minimum(self) -> int:
        curr_price, timestamp = heapq.heappop(self.min_heap)

        while curr_price != self.timestamp_price[timestamp]:
            curr_price, timestamp = heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap, [curr_price, timestamp])
        return curr_price
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna