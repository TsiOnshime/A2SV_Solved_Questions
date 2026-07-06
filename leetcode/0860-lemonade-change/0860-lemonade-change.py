class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5: 0, 10: 0}

        for i in range(len(bills)):
            if bills[i] == 5:
                changes[5] += 1
            elif bills[i] == 10:
                if changes[5] >= 1:
                    changes[5] -= 1
                    changes[10] += 1
                else:
                    return False
            else:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -= 1
                    changes[5] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna