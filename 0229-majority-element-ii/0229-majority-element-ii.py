class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        num_to_frequency = Counter(nums)

        for key, value in num_to_frequency.items():
            if value > (len(nums) // 3):
                res.append(key)
        
        return res

        