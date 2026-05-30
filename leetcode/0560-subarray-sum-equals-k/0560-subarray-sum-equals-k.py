class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = prefix[j] - prefix[l]
        #      currSum      prevSum
        # k - prefix[j] = -prefix[l]
        # prefix[j] - k = prefix[l]
        sum_count = defaultdict(int)
        sum_count[0] = 1
        count = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            prev_sum = running_sum - k

            if prev_sum in sum_count:
                count += sum_count[prev_sum]
            sum_count[running_sum] += 1

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna