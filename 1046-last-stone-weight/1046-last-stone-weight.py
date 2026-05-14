class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        if n == 0:
            return 0
        if n == 1:
            return stones[0]

        # build max heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(stones, i, n)

        # find second largest
        second_idx = 1
        if n > 2 and stones[2] > stones[1]:
            second_idx = 2

        first = stones[0]
        second = stones[second_idx]

        if first == second:
            self.remove(stones, second_idx)
            self.remove(stones, 0)
        else:
            stones[0] = first - second
            self.remove(stones, second_idx)

        return self.lastStoneWeight(stones)

    def remove(self, stones, i):
        stones[i], stones[-1] = stones[-1], stones[i]
        stones.pop()

        n = len(stones)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(stones, i, n)

    def heapify(self, stones, idx, n):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx

        if left < n and stones[left] > stones[largest]:
            largest = left

        if right < n and stones[right] > stones[largest]:
            largest = right

        if largest != idx:
            stones[idx], stones[largest] = stones[largest], stones[idx]
            self.heapify(stones, largest, n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna