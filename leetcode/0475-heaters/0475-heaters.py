class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()

        def calc_distance(i):

            l = 0
            r = len(heaters) - 1

            min_distance = float('inf')

            while l <= r:
                mid = l + (r - l)//2
                min_distance = min(min_distance, abs(heaters[mid] - houses[i]))


                if heaters[mid] >= houses[i]:
                    r = mid - 1
                else:
                    l = mid + 1
            return min_distance

        radius = 0
        for i in range(len(houses)):
            radius = max(radius, calc_distance(i))

        return radius