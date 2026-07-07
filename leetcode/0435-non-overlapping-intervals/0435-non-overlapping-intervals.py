class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start >= last_end:
                last_end = end
            else:
                count += 1
        return count




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna