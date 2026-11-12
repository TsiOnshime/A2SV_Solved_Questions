import math 
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        
        dist = float('inf')

        for i in range(1, math.isqrt(area) + 1):
            num1 = i
            if area % num1 == 0:
                num2 = area // num1
                if num2 - num1 < dist:
                    res = [num2, num1]
                    dist = num2 - num1
        return res
                


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna