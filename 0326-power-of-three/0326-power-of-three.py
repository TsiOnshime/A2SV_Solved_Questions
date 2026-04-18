class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 45 / 3 = 15
        # 15 / 3 = 5
        # 5 / 3 = 1
        self.Truth = True

        def power(num):
            if num != 1 and num < 3:
                self.Truth = False
                return
            if num == 1.0:
                return 

            power(num / 3)
        power(n)
        return self.Truth
                


