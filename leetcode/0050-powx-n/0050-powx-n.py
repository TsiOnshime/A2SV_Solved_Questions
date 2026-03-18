class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        _x = x
        def power(x, n):

            if x == 0:
                return 0
            if  n == 0:
                return 1
            
            res = power(x, n // 2)
            res = res * res
            return x * res if n % 2 else res
        
        res = power(x, abs(n))
        return res if n > 0 else 1 / res


