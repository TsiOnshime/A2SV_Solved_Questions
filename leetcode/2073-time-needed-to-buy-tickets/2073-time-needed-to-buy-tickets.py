class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([i for i in range(len(tickets))])
        time = 0
        while tickets[k] != 0:
            first = queue[0]
            if tickets[first] != 0:
                tickets[first] -= 1
                queue.append(queue.popleft())
                time += 1
            else:
                queue.popleft()
        return time 
