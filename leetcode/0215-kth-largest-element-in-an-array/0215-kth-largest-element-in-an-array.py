class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        for i in range(n// 2 - 1, -1, -1):
            self.max_heapify(nums, i, n)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)

       
        return nums[-k]

    def max_heapify(self, nums, i, n):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and nums[left] > nums[i]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.max_heapify(nums, largest, n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna