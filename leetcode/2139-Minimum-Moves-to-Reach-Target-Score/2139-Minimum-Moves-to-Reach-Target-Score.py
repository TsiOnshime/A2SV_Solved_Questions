class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves  = 0
        while target > 1:
            if not target % 2 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    moves += (target - 1)
                    return moves
                target -= 1
            moves += 1

        return moves