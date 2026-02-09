class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle = num // 3

        if 3 * middle == num:
            return [middle -1 , middle, middle + 1]
        return []