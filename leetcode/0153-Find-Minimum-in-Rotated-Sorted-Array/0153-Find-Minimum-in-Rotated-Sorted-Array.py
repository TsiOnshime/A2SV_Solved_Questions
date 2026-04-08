class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        _min = nums[0]

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[l] <= nums[r]:
                _min = min(_min, nums[l])
                break
            _min = min(_min, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return _min