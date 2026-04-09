class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p,s in zip(position, speed)]

        cars.sort(key = lambda x: x[0], reverse = True)

        print(cars)
        fleet = []
        for car in cars:
            time = (target - car[0]) / car[1]
            if not fleet or fleet[-1] < time:
                fleet.append(time)
        return len(fleet)

        