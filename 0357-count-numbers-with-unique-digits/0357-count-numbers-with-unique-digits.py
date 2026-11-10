class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        prev = 1
      

        def possible_ways(digit):
            ans = 9
            ways = 9
            for i in range(digit - 1):
                ans *= ways
                ways -= 1
            return ans
            
        for i in range(1, n + 1):
            prev = prev + possible_ways(i)
        
        return prev




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna