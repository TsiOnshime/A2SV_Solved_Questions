class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort then use a stack
        
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        
        i = 1
        while stack and i < len(intervals):
            first, second = stack[-1][0], stack[-1][1]
            if second >= intervals[i][0]:
                if second < intervals[i][1]:
                    stack.pop()
                    stack.append([first, intervals[i][1]])
            else:
                stack.append(intervals[i])

            i += 1

        return stack
            

            



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna