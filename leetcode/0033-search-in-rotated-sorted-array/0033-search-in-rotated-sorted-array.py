class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


        l = 0
        r = len(nums) - 1

        ans = -1

        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            elif nums[mid] >=  nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return ans

          
