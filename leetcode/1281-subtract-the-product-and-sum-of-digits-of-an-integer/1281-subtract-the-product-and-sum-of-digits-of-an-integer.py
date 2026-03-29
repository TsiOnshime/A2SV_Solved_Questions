class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        _product = 1
        _sum = 0

        while n:
            _sum += n % 10
            _product *= n % 10
            n //= 10
        return _product - _sum