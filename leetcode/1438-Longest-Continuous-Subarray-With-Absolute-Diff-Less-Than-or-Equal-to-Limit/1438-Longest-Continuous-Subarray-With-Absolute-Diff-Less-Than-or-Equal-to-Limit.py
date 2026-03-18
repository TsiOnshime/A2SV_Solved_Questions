from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        _min = deque() # monotonically increasing queue
        _max = deque() # monotonically decreasing queue
# [5, 4, 3] [6]
# [3, 4, 5] [2]
        length = 0

        l = 0
        for r in range(len(nums)):
            while _max and _max[-1] < nums[r]:
                _max.pop()
            while _min and _min[-1] > nums[r]:
                _min.pop()

            _max.append(nums[r])
            _min.append(nums[r])
            
   
            diff = abs(_max[0] - _min[0])

            while diff > limit :
                if nums[l] == _max[0]:
                    _max.popleft()
                if nums[l] == _min[0]:
                    _min.popleft()
                diff = abs(_max[0] - _min[0]) 
                l += 1
            


            length = max(length, r - l + 1)
        return length