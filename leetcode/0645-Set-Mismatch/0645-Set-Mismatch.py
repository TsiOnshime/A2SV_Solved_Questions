class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        doubled = 0
        missing = 0

        i = 0

        offset = 1

        while i < len(nums):
            swap = nums[i] - offset

            if i == swap:
                i += 1
                continue
            else:
                if nums[i] == nums[swap]:
                    doubled = nums[i]
                    missing = i + 1
                    i += 1
                else:
                    nums[i], nums[swap] = nums[swap], nums[i]

        return [doubled, missing]





# 2 3 3 4 5 6