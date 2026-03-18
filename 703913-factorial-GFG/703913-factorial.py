class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        
        def fact(n):
            if n == 0:
                return 1
            return n * fact(n - 1)
        return fact(n)
    