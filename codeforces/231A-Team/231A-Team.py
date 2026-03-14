q = int(input())

solved = 0
for _ in range(q):
    known = list(map(int, input().split(" ")))
    _sum = sum(known)
    if _sum >= 2:
        solved += 1
    
    
print(solved)