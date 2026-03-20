class Solution:
    def lastRemaining(self, n: int) -> int:
        
# left = True
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# last(4, False)
# last(2, True)
# last(1, False)
# 2* 1 => 2
# 2 * 2 - 1 = > 3
# 2 * 3 => 6

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

        
# O(logn)



        return last(n, True)