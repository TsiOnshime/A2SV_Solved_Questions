class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        picked = {}
        length = 0
        l, r = 0, 0

        while r < len(fruits):
            if fruits[r] in picked:
                picked[fruits[r]] += 1
            else:
                picked[fruits[r]] = 1
            
            if len(picked) > 2:
                picked[fruits[l]] -= 1
                if picked[fruits[l]] == 0:
                    del picked[fruits[l]]
                l += 1
            if len(picked) <= 2:
                length = max(length, r - l + 1)
            r += 1
        return length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna