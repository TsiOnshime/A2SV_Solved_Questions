class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _sum = digits[-1] + 1
        carry = _sum // 10
        last_dig = _sum % 10
        
        digits[-1] = last_dig

        for i in range(len(digits) - 2, -1, -1):
            _sum = digits[i] + carry
            digits[i] = _sum % 10
            carry = _sum // 10

        if carry:
            digits.insert(0, carry)
        return digits


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna