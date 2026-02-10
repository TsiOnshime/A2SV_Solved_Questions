class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        while n not in visited:
            visited.add(n)

            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False

    def sumOfSquares(self, n:int) -> int:

        summ = 0
        while n:
            last_digit = n % 10
            last_digit = pow(last_digit, 2)
            summ += last_digit
            n //= 10
        return summ
