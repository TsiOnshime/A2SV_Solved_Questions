class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = [0] * 3
        # [0,0,0]

        for note in bills:

            if note == 5:
                notes[0] += 1

            elif note == 10:
                if notes[0] > 0:
                    notes[0] -= 1
                else:
                    return False
                notes[1] += 1
            else:
                if notes[1] > 0 and notes[0] > 0:
                    notes[1] -= 1
                    notes[0] -= 1
                elif notes[0] >= 3:
                    notes[0] -= 3
                else:
                    return False
                notes[2] += 1

        return True