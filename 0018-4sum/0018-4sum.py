class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = []
        nums.sort()
        

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    _sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if _sum == target:
                        quads.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif _sum < target:
                        k += 1
                    else: 
                        l -= 1
        
        return quads
                    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna