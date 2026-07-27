class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1

        i = m - 1
        j = n - 1


        while i >= 0 and j >= 0 and idx >= 0:
         
            if nums2[j] >= nums1[i]:
                nums1[idx] = nums2[j]
                j -= 1
                idx -= 1
            else:
                nums1[idx], nums1[i] = nums1[i], nums1[idx]
                i -= 1
                idx -= 1

        while j >= 0:
            nums1[idx] = nums2[j]
            j -= 1
            idx -= 1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna