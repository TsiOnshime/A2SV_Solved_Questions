class Solution:
    def lastRemaining(self, n: int) -> int:
        # Iterative Solution


        # head -> first uneliminated number
        # step -> gap between the uneliminated numbers
        # remaining -> number of elements that are uneliminated
        # left -> direction we're going


        # when does head change?
            # when we go from left to right since we always eliminate the first value
            # when we go from right to left and the number of remaining elements is odd
            # 2, 4, 6 => head was 2 but when we go from right to left we eliminate 6 and 2 -> so head changes to be 4
            # 2, 4 => head is 2 when we go from right to left we eliminate 6 but we are still left with 2 head did not change

        # by what value do we change head when it changes?
        #   when head changes it changes to be the next element which is available and we find that by doing head += step

        # at every loop step will be doubled
        #               remaining elements will be halved


        head = 1
        remaining = n
        step = 1
        left = True

        while remaining > 1:

            if left or remaining % 2 == 1:
                head += step

            step *= 2
            remaining //= 2
            left = not left

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna