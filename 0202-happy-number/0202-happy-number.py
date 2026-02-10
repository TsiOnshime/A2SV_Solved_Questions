class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        summ = 0

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            
            summ = 0
            while n > 0:
                last_digit = n % 10
                n //= 10
                summ += pow(last_digit, 2)
            n = summ
            
        return True