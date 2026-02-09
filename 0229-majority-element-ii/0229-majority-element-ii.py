class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []

        count = Counter(nums)

        result = [keys for keys, value in count.items() if value > (len(nums) // 3)]
       
        return result

        