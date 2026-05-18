class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)

        for key, value in count.items():
            freq[value].append(key)
       
        res = []
        for i in range(len(nums), -1, -1):
            if len(res) == k:
                break
            res.extend(freq[i])

        return res

        

        




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna