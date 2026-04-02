class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        u = sum(weights)


        def possible(capacity):
            total_days = 1
            current_weights = 0

            for weight in weights:
                if current_weights + weight <= capacity:
                    current_weights += weight
                else:
                    current_weights = weight
                    total_days += 1
            return total_days <= days
        
        ans = -1
        while l <= u:
            mid = l + (u - l)//2

            if possible(mid):
                ans = mid
                u = mid - 1
            else:
                l = mid + 1

        return ans