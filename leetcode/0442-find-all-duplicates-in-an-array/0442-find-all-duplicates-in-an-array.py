class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for num in nums:
            n = abs(num)

            nums[n - 1] = -nums[n - 1]

            if nums[n - 1] > 0:
                duplicates.append(n)
        
        return duplicates