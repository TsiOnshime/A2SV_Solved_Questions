class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        output = []
        l = 0
        r = 0

        while r < len(nums):
            if r >= k:
                if queue[0] == nums[l]:
                    queue.popleft()
                l += 1

            if not queue or nums[r] <= queue[-1]:
                queue.append(nums[r])
            else:
                while queue and queue[-1] < nums[r]:
                    queue.pop()
                queue.append(nums[r])
            r += 1
            if r >= k:
                output.append(queue[0])

        return output



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna