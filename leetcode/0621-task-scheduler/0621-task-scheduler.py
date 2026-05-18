class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        offset = 65
        minHeap = []
        queue = deque()

        for i in range(len(tasks)):
            
            letter = ord(tasks[i]) - offset
            count[letter] += 1

        for i in range(len(count)):
            if count[i] != 0:
                heapq.heappush(minHeap, -count[i])

        print(minHeap)
        # [-1]
        # time = 5
        # q = [[-1, 7]]
        #
        time = 0
        while minHeap or queue:
            time += 1
            if minHeap:
                freq = heapq.heappop(minHeap)
                if freq + 1 != 0:
                    queue.append([freq + 1, time + n])
            if queue and queue[0][1] == time:
                freq, t = queue.popleft()
                heapq.heappush(minHeap,freq)
    
        return time 

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna