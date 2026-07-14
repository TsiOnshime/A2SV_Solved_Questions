class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []

        for i in range(len(nums)):
            if nums[i][i] == "0":
                ans.append("1")
            else:
                ans.append("0")
        return "".join(ans)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna