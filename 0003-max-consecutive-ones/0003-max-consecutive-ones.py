class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                max_count = max(count, max_count)
        
        return max_count