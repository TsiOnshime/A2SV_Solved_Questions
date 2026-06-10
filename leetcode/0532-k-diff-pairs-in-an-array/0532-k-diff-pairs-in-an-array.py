class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        if k == 0:
            for key, val in freq.items():
                if val > 1:
                    count += 1
        
        else:
            for key, val in freq.items():
                b = key + k
                if b in freq:
                    count += 1

        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna