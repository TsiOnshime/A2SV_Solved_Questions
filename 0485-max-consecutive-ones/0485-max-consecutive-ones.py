class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                _max = max(count, _max)
        return _max
            
            
                
            