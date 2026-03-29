class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        
        output = start + (2 * 0)

        
        for i in range(1, n):
            output ^= (start + (2 * i))

        return output