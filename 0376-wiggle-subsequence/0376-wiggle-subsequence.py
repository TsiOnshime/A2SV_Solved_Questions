class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        
        max_length = 0
        cache = {}
        def check(prev, sign, start):
            nonlocal cache
            nonlocal max_length
            if start == len(nums):
                return 0
            if (prev, sign, start) in cache:
                return cache[(prev, sign, start)]

            max_count = 0
            for i in range(start, len(nums)):
                diff = nums[i] - prev
                if diff == 0:
                    continue
                curr_sign = "-" if diff < 0 else "+"
                if curr_sign == sign:
                    continue
                count = 1 + check(nums[i], curr_sign, i + 1)
                
                max_count = max(max_count, count)
            # max_length = max(max_length, count)
            cache[(prev, sign, start)] =  max_count
            return max_count 
        

        for i in range(len(nums)):
            count = max(1 + check(nums[i], "+", i + 1), 1 + check(nums[i], "-", i + 1))
            max_length = max(max_length, count)
        return max_length 





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna