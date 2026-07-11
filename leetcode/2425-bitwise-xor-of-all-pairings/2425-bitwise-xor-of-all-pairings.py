class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums2)
        xor = 0

        num2Xor = 0
        for i in range(len(nums2)):
            num2Xor ^= nums2[i]


        for i in range(len(nums1)):
            if n & 1:
                xor ^= nums1[i]
        if len(nums1) & 1:
            xor ^= num2Xor
        return xor

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna