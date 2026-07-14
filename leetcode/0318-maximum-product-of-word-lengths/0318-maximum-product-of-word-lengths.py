class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = [[0, 0]]
        ans = 0
        for word in words:
            state = 0
            for ch in word:
                state |= (1 << (ord(ch) - 97))    
            masks.append([state, len(word)])
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i][0] & masks[j][0]:
                    continue
                prod = masks[i][1] * masks[j][1]
                ans = max(ans, prod)

        return ans

            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna