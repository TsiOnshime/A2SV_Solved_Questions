from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic decreasing queue
        # if we get an element that is greater than the top element of our queue we pop
        # if the left pointer is out of bounds we pop from the zeroth index
        # how do we check if left is out of bounds?
            # if the index at the zeroth index in our queue is less than our left index that means the que[0] is out of bounds
        # how do we append an element to our output?
            # if r + 1 is greater than or equal to k that means our right pointer has reached the window of 3 so we append queue[0] and increase the value of right pointer
        # at each iteration we increment the value of our left pointer by 1
        queue = deque()
        output = []

        l = r = 0
        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            
            if l > queue[0]:
                queue.popleft()
            if r + 1 >= k:
                output.append(nums[queue[0]])
                l += 1

            r += 1
        return output
        