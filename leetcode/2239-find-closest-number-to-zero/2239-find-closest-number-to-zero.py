class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dis = float('inf')
        num = []


        for i in range(len(nums)):
            if dis > abs(nums[i] - 0):
                dis = abs(nums[i] - 0)
                num = nums[i]
            elif dis == abs(nums[i] - 0):
                if nums[i] > num:
                    num = nums[i]
    
        return num
