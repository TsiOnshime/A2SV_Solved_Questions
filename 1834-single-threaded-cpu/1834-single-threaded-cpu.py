class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()
        i = 0
        time = tasks[0][0]
        min_heap = []
        order = []
        while i < len(tasks) or min_heap:
            
            if min_heap:
                p, idx = heapq.heappop(min_heap)
                order.append(idx)
                time += p
            else:
                time = tasks[i][0]
            while i < len(tasks) and time >= tasks[i][0]:
                p, j = tasks[i][1], tasks[i][2]
                heapq.heappush(min_heap, [p, j])
                i += 1

        return order

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna