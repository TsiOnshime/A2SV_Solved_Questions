class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, n):

            if n == 0:
                return 1
            if x == 0:
                return 0
            res = power(x, n//2)
            res = res * res
            if n % 2:
                return x * res
            else:
                return res

        
        res = power(x, abs(n))
        return res if n >= 0 else 1/res

