class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        duplicate = []
        for num in nums:
            arr[num] += 1
            if arr[num] > 1:
                duplicate.append(num)

        return duplicate

        
