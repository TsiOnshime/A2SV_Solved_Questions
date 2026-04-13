class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # TTTTTFFFFFF
        # candies given = 1 ----- sum(candies) // k
        def possible(mid):
            count = 0
            for candy in candies:
                if candy >= mid:
                    count += candy // mid
            return count >= k


        l = 1
        r = sum(candies) // k

        ans = 0
        while l <= r:
            mid = l + (r - l)//2
            if possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans