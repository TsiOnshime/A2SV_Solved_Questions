class Solution:
    def mySqrt(self, x: int) -> int:
        
        l = 0
        u = x
        ans = 0

        while l <= u:
            mid = (l + u) // 2

            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                u = mid - 1
        return ans
            