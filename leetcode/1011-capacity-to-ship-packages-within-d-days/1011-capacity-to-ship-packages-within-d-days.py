class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible(capacity):
            total_day = 1

            curr = 0
            i = 0
            while i < len(weights):
                if curr + weights[i] > capacity:
                    total_day += 1
                    curr = 0
                
                curr += weights[i]
                i += 1
            return total_day


        

        l = max(weights)
        u = sum(weights)
        ans = 0
        while l <= u:
            mid = (l + u) // 2


            if possible(mid) > days:
                l = mid + 1
            else:
                u = mid - 1

        return l