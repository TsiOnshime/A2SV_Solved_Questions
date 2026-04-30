from collections import defaultdict, deque
import sys
input = sys.stdin.readline
n = int(input())

adj_list = [[] for i in range(n + 1)]
for i in range(n - 1):
    u, v = list(map(int, input().split()))

    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(start):
    queue = deque()
    visited = [False] * (n)
    queue.append((start, 0))
    visited[start - 1] = True
    
    while queue:
        node, level = queue.popleft()
        for neigh in adj_list[node]:
            if not visited[neigh - 1]:
                visited[neigh - 1] = True
                queue.append((neigh, level + 1))
                
    return node, level
        
        

first_end, diameter1 = bfs(1)
second_end, diameter = bfs(first_end)
    
print(diameter * 3)