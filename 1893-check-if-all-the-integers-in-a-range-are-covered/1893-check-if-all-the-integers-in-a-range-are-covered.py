class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [0] * 51

        for i in range(len(ranges)):
            start = ranges[i][0]
            end = ranges[i][1]

            for x in range(start, end + 1):
                arr[x] = 1

        for x in range(left, right + 1):
            if arr[x] != 1:
                return False

        return True
