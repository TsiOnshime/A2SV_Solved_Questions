from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)

        appearing_once = ("").join([key for key, value in count.items() if value == 1])
        if len(appearing_once) == 0:
            return - 1


        return s.index(appearing_once[0])
        