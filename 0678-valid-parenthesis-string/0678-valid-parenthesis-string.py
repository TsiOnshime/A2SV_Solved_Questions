class Solution:
    def checkValidString(self, s: str) -> bool:

        _min = 0 # represents the minimum number of opening brackets till i
        _max = 0 # represents the maximum number of opening brackets till i

        for i in range(len(s)):
            if s[i] == "(":
                _min += 1
                _max += 1
            elif s[i] == ")":
                _min -= 1
                _max -= 1
            else:
                _min -= 1
                _max += 1
            if _min < 0:
                _min = 0
            if _max < 0:
                return False
        return _min == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna