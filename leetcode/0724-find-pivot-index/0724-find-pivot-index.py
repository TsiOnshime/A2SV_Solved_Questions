class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # [1,7,3,6,5,6]
        # 0 and 7 + 3 + 6 + 5 + 6 = 27
        # 1 and 3 + 6 + 5 + 6 = 24
        # 1 + 7 = 8 and 6 + 5 + 6 = 17
        # 1 + 7 + 3 = 11 and 5 + 6 = 11
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        left = 0
        right = 0
        for i in range(len(nums)):
            if i == 0:
                left = 0 
            else:
                left = nums[i - 1]
            right = nums[len(nums) - 1] - nums[i]
            if left == right:
                return i
        return -1
