class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {n: i for i, n in enumerate(nums1)}
        stack = []
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                popped = stack.pop()
                if popped in hashMap:
                    res[hashMap[popped]] = nums2[i]
            
            if nums2[i] in hashMap:
                stack.append(nums2[i])

        return res