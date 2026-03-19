class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [1,2, 5, 6]
        # target = 3
        
        def binary(l, r):
            if l > r:
                return -1
            middle = (r + l) // 2
            if nums[middle] < target:
                l = middle + 1
                return binary(l, r)
            elif nums[middle] > target:
                r = middle - 1
                return binary(l, r)
            else:
                return middle

            



        return binary(0, len(nums) - 1)