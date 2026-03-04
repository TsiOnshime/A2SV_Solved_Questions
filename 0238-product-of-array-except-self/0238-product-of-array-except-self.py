class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix_prod = [1, 1, 2, 6]
        # surrix_prod = [24,12,4,1]
        # prod = [24, 12, 8, 6]

        # prefix_prod = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     prefix_prod[i] = nums[i - 1] * prefix_prod[i - 1]

        # suffix_prod = [1] * len(nums)
        # for i in range(len(nums) - 2, -1, -1):
        #     suffix_prod[i] = nums[i + 1] * suffix_prod[i + 1]

        # prod = [0] * len(nums)
        # for i in range(len(nums)):
        #     prod[i] = prefix_prod[i] * suffix_prod[i]
        
        # return prod

        prod = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            prod[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= postfix
            postfix *= nums[i]
        return prod