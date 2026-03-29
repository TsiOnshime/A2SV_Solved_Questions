class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num:
                digit_sum += num % 10
                num //= 10
        print(element_sum)
        print(digit_sum)
        return abs(digit_sum - element_sum)