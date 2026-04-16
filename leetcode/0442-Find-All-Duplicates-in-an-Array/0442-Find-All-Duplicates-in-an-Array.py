class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()

        offset = 1
        i = 0

        while i < len(nums):
            correct_idx = nums[i] - offset
            if i == correct_idx:
                i += 1
                continue
            else:
                if nums[i] == nums[correct_idx]:
                    duplicates.add(nums[i])
                    i += 1
                else:
                    nums[i], nums[correct_idx]= nums[correct_idx], nums[i]
        
        return list(duplicates)