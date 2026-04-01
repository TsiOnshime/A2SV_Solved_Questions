class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        l = 0
        r = len(nums) - 1
        ans = [-1, -1]
        while l <= r:
            mid = (l + r) // 2
           
            if target == nums[mid]:     
                l = r = mid
                while l >= 0 and nums[l] == target:
                    ans[0] = l
                    l -= 1
                while r < len(nums) and nums[r] == target:
                    ans[1] = r
                    r += 1
                break
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans
