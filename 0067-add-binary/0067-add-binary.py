class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0

        j = len(a) - 1
        i = len(b) - 1
        res = []
        while j >= 0 or i >= 0 or carry:
            val1 = int(a[j]) if j >= 0 else 0
            val2 = int(b[i]) if i >= 0 else 0

            total = val1 + val2 + carry
            
            if total == 0:
                res.append("0")
            elif total == 1:
                res.append("1")
                carry = 0
            elif total == 2:
                res.append("0")
                carry = 1
            else:
                res.append("1")
                carry = 1

            j -= 1
            i -= 1
        return "".join(list(reversed(res)))
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna