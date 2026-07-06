class Solution:
    def solve(self, bt):
        bt.sort()
        waiting_time = 0
        time = 0
        for i in range(len(bt)):
            
            waiting_time += time
            time += bt[i]
        return waiting_time // len(bt)
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna