class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # TTTTTFFFFF
        position.sort()
        # possible distances
        l, r = 1, position[-1] - position[0]

        def possible(mid):
            count = 1
            prev = 0
            j = 1
            while j < len(position):
                if position[j] - position[prev] >= mid:
                    count += 1
                    prev = j 
                j += 1
            return count >= m

            
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2

            if possible(mid): 
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans