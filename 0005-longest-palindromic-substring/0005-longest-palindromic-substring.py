class Solution:
    def longestPalindrome(self, string: str) -> str:
        max_length = 0
        s, e = 0, 0
        # index of middle element
        def findMax(j, k):
            while j >= 0 and k < len(string) and string[j] == string[k]:
                j -= 1
                k += 1
            return [k - j + 1 - 2, j, k]
        for i in range(len(string)):
            # when it is the middle
            j, k = i - 1, i + 1
            res, st, en = findMax(j, k)
            if res > max_length:
                max_length = res
                s, e = st, en
            
            j, k = i, i + 1
            res, st, en = findMax(j, k)
            if res > max_length:
                max_length = res
                s, e = st, en
            j, k = i - 1, i
            res, st, en = findMax(j, k)
            if res > max_length:
                max_length = res
                s, e = st, en
            # when it is the left char
            
            # when it is the right char
        return string[s + 1:e]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna