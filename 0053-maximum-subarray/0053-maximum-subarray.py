class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The basic insight is negative number has no contribution in increasing the value of our sum so when the prefix sum before a number is negative we disregard the sum up until that number and start calculating the sum again
        keep a running sum 
        a max_sum 
        and iterate through nums
        if our running_sum is less than zero we reset it to be zero
        and 
         [-2,1,-3,4,-1,2,1,-5,4]
        0 -2 1 -2 4  3  5 6 1 5
    running_sum

        after that we calculate  the running_sum again as += num
        then we get the max_sum = max(max_sum, running_sum)
        """

        running_sum = 0
        max_sum = nums[0]

        for num in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum += num
            max_sum = max(max_sum, running_sum)
        return max_sum


        """
        [5,4,-1,7,8]
        | running_sum |  max_sum  |
        |      0      |      5    |
        |      5      |      5    |
        |      9      |      9    |
        |      8      |      9    |
        |      15     |     15    |
        |      23     |     23    |
        """