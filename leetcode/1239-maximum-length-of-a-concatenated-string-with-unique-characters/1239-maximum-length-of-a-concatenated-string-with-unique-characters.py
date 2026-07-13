class Solution:
    def maxLength(self, arr: List[str]) -> int:
        subsequences = 1 << len(arr)
        max_length = 0

        for i in range(subsequences):
            prev = set()
            length = 0
            for j in range(len(arr)):
                if i & (1 << j):
                    for k in range(len(arr[j])):
                        if arr[j][k] in prev:
                            break
                        else:
                            prev.add(arr[j][k])
                    else:
                        length += len(arr[j])

            max_length = max(max_length, length)
        return max_length
                    




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna