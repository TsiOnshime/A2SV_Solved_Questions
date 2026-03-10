class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,7,3,6,5,6]
        # 0 and 7 + 3 + 6 + 5 + 6 = 27
        # 1 and 3 + 6 + 5 + 6 = 24
        # 1 + 7 = 8 and 6 + 5 + 6 = 17
        # 1 + 7 + 3 = 11 and 5 + 6 = 11
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left += nums[i]
            
        return -1
