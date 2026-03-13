from collections import deque
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flipq = deque()
        count = 0
 
        for i in range(len(nums)):
            while flipq and flipq[0] + 2 < i:
                flipq.popleft()
            
            if (nums[i] + len(flipq)) % 2 == 0:
                if i + 2 >= len(nums):
                    return -1
                count += 1
                flipq.append(i)
        
        return count

