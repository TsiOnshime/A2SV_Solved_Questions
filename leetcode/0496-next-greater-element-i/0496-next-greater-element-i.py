class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = defaultdict(lambda: -1)
        res =[]
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            nge[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])

        for i in range(len(nums1)):
            res.append(nge[nums1[i]])
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna