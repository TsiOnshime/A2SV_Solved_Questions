class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [[0, 0]] # mask, concatenated words len
        ans = 0
        for word in arr:

            state = 0
            valid = True
            for ch in word:
                if not state & (1 << (ord(ch) - 97)):
                    state |= (1 << (ord(ch) - 97))
                else:
                    valid = False
            if not valid:
                continue

            
            n = len(masks)
            
            for i in range(n):
                mask, length = masks[i]
                if mask & state:
                    continue
                
                masks.append([mask | state, length + len(word)])
                ans = max(ans, length + len(word))

        return ans
                
                
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna