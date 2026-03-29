class Solution:
    def judgeCircle(self, moves: str) -> bool:


        start = [0, 0]

        for i in moves:
            if i == "U":
                start[0] += 1
            if i == "D":
                start[0] -= 1
            if i == "R":
                start[1] += 1
            if i == "L":
                start[1] -= 1
        if start == [0, 0]:
            return True
        return False