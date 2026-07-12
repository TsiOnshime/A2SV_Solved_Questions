class Solution:
    def isHappy(self, n: int) -> bool:
        def nextHappy(n):
            _sum = 0
            while n:
                _sum += (n % 10) ** 2
                n //= 10

            return _sum
        tortoise = n
        hare = nextHappy(n)

        while tortoise != hare:
            if tortoise == 1:
                return True
            tortoise = nextHappy(tortoise)
            hare = nextHappy(nextHappy(hare))
        return tortoise == 1



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna