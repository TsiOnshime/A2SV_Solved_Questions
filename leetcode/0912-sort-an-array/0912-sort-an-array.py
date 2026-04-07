class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge(left_half, right_half):
            l = r = 0
            temp = []
            while l < len(left_half) and r < len(right_half):
                if left_half[l] <= right_half[r]:
                    temp.append(left_half[l])
                    l += 1
                else:
                    temp.append(right_half[r])
                    r += 1
            while l < len(left_half):
                temp.append(left_half[l])
                l += 1
            while r < len(right_half):
                temp.append(right_half[r])
                r += 1
            return temp
        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            
            mid = left + (right - left) // 2
            left_part = mergeSort(left, mid)
            right_part = mergeSort(mid + 1, right)

            return merge(left_part, right_part)
        

        return mergeSort(0, len(nums) - 1)