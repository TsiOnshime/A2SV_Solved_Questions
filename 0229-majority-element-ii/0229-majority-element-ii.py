class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        count1 = 0
        elem1 = 0

        count2 = 0
        elem2 = 0

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != elem2:
                count1 = 1
                elem1 = nums[i]
            elif count2 == 0 and nums[i] != elem1:
                count2 = 1
                elem2 = nums[i]
            elif nums[i] == elem1:
                count1 += 1
            elif nums[i] == elem2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for i in range(len(nums)):
            if nums[i] == elem1:
                count1 += 1
            elif nums[i] == elem2:
                count2 += 1
        if count1 > len(nums) // 3:
            res.append(elem1)
        if count2 > len(nums) // 3:
            res.append(elem2)
        return res


        
            

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna