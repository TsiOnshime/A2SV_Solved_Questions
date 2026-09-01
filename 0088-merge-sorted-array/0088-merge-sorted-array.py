class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # 2
        j = n - 1 # 2
        last = m + n - 1 # 5

        while i >= 0 or j >= 0:
            n1 = nums1[i] if i >= 0 else float('-inf') # 3
            n2 = nums2[j] if j >= 0 else float('-inf') # 6
            if n1 > n2:
                nums1[last] = n1
                i -= 1
            else:
                nums1[last] = n2
                j -= 1
            last -= 1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna