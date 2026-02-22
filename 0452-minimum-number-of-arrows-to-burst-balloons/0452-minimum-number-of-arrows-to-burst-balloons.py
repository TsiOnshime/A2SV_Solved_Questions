class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        """
        First assume the shots we need is equal to the number of elements of points

        order the points in increasing order based on x-start

        store the first point as prev

        iterate through the points starting from 1-len(points)

        store the current point in a variable curr 

        compare curr[0] and prev[1]:

        if curr[0] is less than or equal to prev[1]:
            shot -= 1
            prev = [prev[0], min(prev[1], curr[1])]

        """

        shots = len(points)
        points.sort()

        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]:
                shots -= 1
                prev = [curr[0], min(prev[1], curr[1])]
            else:
                prev = curr

        return shots