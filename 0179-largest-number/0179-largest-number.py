class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        Arranges a list of non-negative integers to form the largest number.

        Args:
            nums: The list of non-negative integers.

        Returns:
            The largest number formed as a string.
        """
        from functools import cmp_to_key

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            else:
                return 0

        nums_str = [str(num) for num in nums]
        nums_str.sort(key=cmp_to_key(compare))

        result = "".join(nums_str)
        if result[0] == '0':
            return '0'
        return result