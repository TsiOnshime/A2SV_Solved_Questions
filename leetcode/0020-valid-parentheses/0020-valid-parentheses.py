class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for br in s:
            if br in {"(", "[", "{"}:
                stack.append(br)
            else:
                if not stack or stack[-1] != pairs[br]:
                    return False
                stack.pop()
        
        return True if not stack else False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna