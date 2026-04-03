class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.append(float('inf'))
        heaters.append(float('-inf'))

        heaters.sort()
        houses.sort()

        radius = 0
        min_distance = float('inf')

        j = 0
        for i in range(len(houses)):

            while heaters[j] < houses[i]:
                j += 1
            if j > len(heaters):
                break

            left_dist = float('inf') if heaters[j - 1] == float('-inf') else abs(heaters[j-1] - houses[i])
            right_dist = float('inf') if heaters[j] == float('inf') else abs(heaters[j] - houses[i])
            min_distance = min(left_dist, right_dist)

            radius = max(radius, min_distance)

        return radius



