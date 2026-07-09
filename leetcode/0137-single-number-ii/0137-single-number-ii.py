class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            count = 0
            for j in nums:
                # check if ith bit is set
                if j & (1 << i):
                    count += 1
            if count % 3 == 1:
                # if the sigh bit is set
                if i == 31:
                    # we decrement what we have been working on by 2**31 so that we could get the negative number 
                    ans -= (1 << i)
                else:
                    # set ith bit
                    ans = ans | (1 << i)
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna