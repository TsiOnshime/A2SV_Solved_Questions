class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for key, val in freq.items():
            if k == 0:
                if val >= 2:
                    count += 1
            else:
                otherval = key + k
                if otherval in freq:
                    count += 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna