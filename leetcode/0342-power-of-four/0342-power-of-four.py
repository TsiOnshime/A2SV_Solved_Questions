class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def pow_four(n):
            if n == 1.0:
                return 1
            elif n < 4.0:
                return 0
            
            return pow_four(n/4)
        n = pow_four(n)
        if n == 1:
            return True
        return False
            