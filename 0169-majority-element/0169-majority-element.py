class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate = 0
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            else:
                if candidate == i:
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        candidate = i
                        count = 1
        return candidate

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna