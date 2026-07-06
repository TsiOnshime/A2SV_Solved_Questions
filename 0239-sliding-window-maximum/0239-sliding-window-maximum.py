class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
   
        for i in range(len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i + 1 >= k:
                res.append(queue[0])
                if i - k + 1 >= 0 and nums[i - k + 1] == queue[0]:
                    queue.popleft()
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna