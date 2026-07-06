class StockSpanner:

    def __init__(self):
        self.stack = []

        
        
    def next(self, price: int) -> int:
        self.span = 1
        while self.stack and self.stack[-1][0] <= price:
            p, s = self.stack.pop()
            self.span += s

        self.stack.append([price, self.span])
      
        return self.span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna