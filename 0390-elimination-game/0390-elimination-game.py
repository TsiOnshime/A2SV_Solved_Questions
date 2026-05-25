class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def last(n, left):
            if n == 1:
                return 1
            
            if left:
                return 2 * last(n // 2, False)
            else:
                if n % 2:
                    return 2 * last(n // 2, True)
                else:
                    return 2 * last(n // 2, True) - 1


        
        return last(n, True)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna