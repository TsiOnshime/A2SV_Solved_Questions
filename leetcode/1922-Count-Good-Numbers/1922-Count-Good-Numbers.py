class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        even = n - odd
        mod = 10 ** 9 + 7

        def power(x, y):

            if y == 0:
                return 1
            
            res = power(x, y//2)
            res *= res
            res %= mod
            if y % 2:
                res *= x
            res %= mod

            return res
        
        possibilities = (power(5 , even) * power(4, odd)) % mod

        return possibilities