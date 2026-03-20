class Solution:
    def lastRemaining(self, n: int) -> int:
        
# left = True

        def last(n, left):
            if n == 1:
                return 1
            
            if left:
                return 2 * last(n//2, False)
            else:
                if n % 2:
                    return 2 * last(n//2, True)
                else:
                    return 2 * last(n//2, True) - 1

        



        return last(n, True)