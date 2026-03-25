class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all possible permutations of a list of distinct integers.

        Args:
            nums: The list of distinct integers.

        Returns:
            A list of all possible permutations.
        """
        result = []

        def backtrack(current_permutation: list[int], remaining_nums: list[int]):
            if not remaining_nums:  # Base case: all numbers have been used
                result.append(current_permutation[:])  # Append a copy
                return

            for i in range(len(remaining_nums)):
                # Choose a number from the remaining numbers
                num = remaining_nums[i]

                # Create a new permutation and remaining numbers
                new_permutation = current_permutation + [num]
                new_remaining_nums = remaining_nums[:i] + remaining_nums[i + 1:]

                # Recursively generate permutations
                backtrack(new_permutation, new_remaining_nums)

        backtrack([], nums)
        return result