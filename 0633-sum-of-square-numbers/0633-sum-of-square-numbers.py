class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False
        

        
        l = 0
        r = int(sqrt(c))

        while l <= r:
            summ = (l ** 2) + (r ** 2)
           
            if summ == c:
                return True
            elif summ < c:
                l += 1
            else:
                r -= 1
        return False
            