from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = deque()
        res = float('inf')

        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]

            if curr_sum >= k:
                res = min(res, r + 1)
            while dq and curr_sum - dq[0][0] >= k:
                prefix, l = dq.popleft()
                res = min(res, r - l)
            while dq and dq[-1][0] > curr_sum:
                dq.pop()
            dq.append([curr_sum, r])
        return -1 if res == float('inf') else res