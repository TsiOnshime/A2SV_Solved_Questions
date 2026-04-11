class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
     # to calculate ceil(pile/k) we can do (piles + k - 1) // k

        def possible(mid):
            time = 0

            for pile in piles:
                time += math.ceil(pile / mid)
            return time <= h


        l = 1 
        r = max(piles)

        ans = 0

        while l <= r:

            mid = l + (r - l)//2
            if possible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans