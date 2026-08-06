class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        start = 0
        end = n - 1

        adj_list = defaultdict(list)

        for u, v, t in roads:
            adj_list[u].append([v, t])
            adj_list[v].append([u, t])

        ways = [0] * n
        ways[start] = 1
        min_time = [float('inf')] * n
        min_time[start] = 0

        min_heap = []
        heapq.heappush(min_heap, [0, 0])

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > min_time[node]:
                continue
            for neigh, t in adj_list[node]:
                if min_time[neigh] == time + t:
                    ways[neigh] += ways[node]
                elif min_time[neigh] > time + t:
                    ways[neigh] = ways[node]
                    min_time[neigh] = time + t
                    heapq.heappush(min_heap, [time + t, neigh])
        return ways[end] % (10**9 + 7)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna