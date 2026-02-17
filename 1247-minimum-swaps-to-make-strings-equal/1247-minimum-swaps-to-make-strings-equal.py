class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        '''
        Three cases:
        xy - 2 => 1 swap
        yx - 2 => 1 swap

        yx and xy => 2 swap
        '''
        xy = 0
        yx = 0


        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
                print(xy, i)
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1
                print(yx, i)
            else:
                continue

        if (xy + yx) % 2:
            return -1

        swap = (xy // 2) + (yx // 2)

        xy %= 2
        yx %= 2

        if xy == 1 and yx == 1:
            swap += 2
        return swap