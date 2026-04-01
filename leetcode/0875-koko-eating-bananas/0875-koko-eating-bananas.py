class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def possible(k):
            time = 0
            for pile in piles:
                time += (pile + k - 1) // k 
            return time

        l = 1
        u = max(piles)
        while l <= u:
            mid = l + (u - l)// 2 
            needed = possible(mid)
            if needed > h:
                l = mid + 1
            else:
                u = mid - 1
        return l
o = Solution()
print(o.minEatingSpeed([30,11,23,4,20], 5))