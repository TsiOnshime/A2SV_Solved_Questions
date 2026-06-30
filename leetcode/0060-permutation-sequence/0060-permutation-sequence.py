class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []
        num = []
        fact = 1
        # fact -> tells us number of permutiations we could make with the rest of the numbers after we take one number to be the leading number
        for i in range(1, n + 1):
            numbers.append(str(i))
            if i != n:
                fact *= i
        k -= 1
        
        first_number = numbers[k // fact]
        num.append(first_number)
        numbers.pop(k // fact)
        
        while numbers:

            k %= fact
            fact //= len(numbers)
            num.append(numbers.pop(k // fact)) 

        return "".join(num)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna