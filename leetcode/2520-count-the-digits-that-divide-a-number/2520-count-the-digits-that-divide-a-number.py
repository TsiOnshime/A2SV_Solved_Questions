class Solution:
    def countDigits(self, num: int) -> int:
        new_num = num
        count = 0
        while new_num:
            if num % (new_num % 10) == 0:
                count += 1
            new_num //= 10
        return count