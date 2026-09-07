class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        count = defaultdict(int)
        for i in range(len(nums)):
            count[nums[i]] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
                if c > 1:
                    new_count[n] = c - 1
            
            count = new_count
        

        res = []

        for n in count:
            if nums.count(n) > len(nums)//3:
                res.append(n)
        return res
            
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna