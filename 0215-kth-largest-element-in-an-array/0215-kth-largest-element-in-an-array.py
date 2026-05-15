class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
        while len(heap) < k:
            heapq.heappush(heap, nums[i])
            i += 1

        while i < len(nums):
            if heap[0] < nums[i]:
                heapq.heapreplace(heap,nums[i])
            i += 1
            
        return heap[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna