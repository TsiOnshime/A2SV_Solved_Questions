class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        def binarySearch(first):

            l = 0
            r = len(first) - 1

            while True:
                i = (l + r) // 2 # for pointing to first array
                j = half - i - 2

                firstLeft = first[i] if i >= 0 else float('-inf')
                firstRight = first[i + 1] if i + 1 < len(first) else float('inf')
                secondLeft = second[j] if j >= 0 else float('-inf')
                secondRight = second[j + 1] if j + 1 < len(second) else float('inf')

                if firstLeft <= secondRight and secondLeft <= firstRight:
                    if total % 2:
                        return min(secondRight, firstRight)
                    return (max(firstLeft, secondLeft) + min(firstRight, secondRight)) / 2
                elif firstLeft > secondRight:
                    r = i - 1
                else:
                    l = i + 1

        if len(nums1) < len(nums2):
            second = nums2
            return binarySearch(nums1)
        else:
            second = nums1
            return binarySearch(nums2)

