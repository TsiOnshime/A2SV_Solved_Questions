class Solution:
    def countDigits(self, num: int) -> int:
        s_num = str(num)
        count = 0

        for i in s_num:
            if num % int(i) == 0:
                count += 1
        
        return count