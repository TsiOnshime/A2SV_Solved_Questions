class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.probability = [0] * len(w)

        _sum = sum(self.w)
        self.probability[0] = self.w[0] // _sum
        for i in range(1, len(self.w)):
        
            self.probability[i] = self.probability[i - 1] + (self.w[i] / _sum)
        
    def pickIndex(self) -> int:
        target = random.uniform(0, 1)
        left = 0
        right = len(self.w) - 1
        ans = 0

        while left <= right:

            mid = left + (right - left)//2
            if self.probability[mid] < target:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna