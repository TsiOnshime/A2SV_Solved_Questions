class Solution:
    def isBalanced(self, s):
        # code here
        
        stack = []
        
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        
        for br in s:
            if br in {"[", "{", "("}:
                stack.append(br)
            else:
                if not stack or stack[-1] != pairs[br]:
                    return False
                else:
                    stack.pop()
                    
        if not stack:
            return True
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna