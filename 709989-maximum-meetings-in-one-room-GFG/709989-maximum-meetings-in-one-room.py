class Solution:
    def maxMeetings(self, s, f) :
        # code here
        order = []
        
        meetings = []
        for i in range(len(s)):
            meetings.append([f[i], i, s[i]])
        
        meetings.sort()
        
        order.append(meetings[0][1] + 1)
        last_meeting = meetings[0][0]
        
        for i in range(1, len(s)):
            end, ind, start = meetings[i]
            if start > last_meeting:
                last_meeting = end
                order.append(ind + 1)
        order.sort()
        return order
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna