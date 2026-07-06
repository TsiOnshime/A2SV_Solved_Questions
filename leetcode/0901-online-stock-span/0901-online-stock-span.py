class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = []
        self.index = 0
        
        
    def next(self, price: int) -> int:
        self.individual_count = 0
        while self.stack and self.stack[-1][0] <= price:
            elem, ind = self.stack.pop()
            self.individual_count += self.count[ind]
        self.count.append(self.individual_count + 1)
        self.stack.append([price, self.index])
        self.index += 1
        return self.count[-1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna