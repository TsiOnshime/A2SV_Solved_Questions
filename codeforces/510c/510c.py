from collections import deque
order = []
n = int(input())
graph = {}
indegree = [0] * 26
for i in range(97, 123):
    graph[chr(i)] = []

names = []
for i in range(n):
    names.append(input())
impossible = False
for i in range(n - 1):
    j = 0
    name1 = names[i]
    name2 = names[i + 1]
    
    while j < min(len(name1), len(name2)) and name1[j] == name2[j]:
        j += 1
   
    if j == len(name2) and len(name1) > len(name2):
        impossible = True
        break
    if j < min(len(name1), len(name2)):
        graph[name1[j]].append(name2[j])
        indegree[ord(name2[j]) - 97] += 1
if impossible:
    print("Impossible")   
else:
    queue = deque()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(chr(i + 97))
    while queue:
        node = queue.popleft()
        order.append(node)
        for neigh in graph[node]:
            indegree[ord(neigh) - 97] -= 1
            if indegree[ord(neigh) - 97] == 0:
                queue.append(neigh)
    order = "".join(order)
    if len(order) != 26:
        print("Impossible")
    else:
        print(order)