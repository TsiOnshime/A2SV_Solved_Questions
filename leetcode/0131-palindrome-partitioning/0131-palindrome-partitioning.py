class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                r -= 1
                l += 1
            return True
        def palindrome(idx, state):
            nonlocal res
            if idx == len(s):
                res.append(state.copy())
                return


            for i in range(idx, len(s)):
                if check(idx, i):
                    state.append(s[idx:i + 1])
                    palindrome(i + 1, state)
                    state.pop()
        palindrome(0, [])
        return res
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna