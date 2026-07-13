class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == (-1 << 31) and divisor == -1:
            return (1 << 31) - 1
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        for shift in range(31, -1, -1):
            if dividend >= (divisor << shift):
                quotient += (1 << shift)
                dividend -= (divisor << shift)
        return sign * quotient


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna