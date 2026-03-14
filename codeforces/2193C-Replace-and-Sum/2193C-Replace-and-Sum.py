t = int(input())
for _ in range(t):
    n, q = map(int, input().split(" "))
    
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    
    if a[-1] < b[-1]:
        a[-1], b[-1] = b[-1], a[-1]
        
    for i in range(n-2, -1, -1):
        _max = max(a[i], b[i], a[i + 1])
        a[i] = _max
    for i in range(1, len(a)):
        a[i] += a[i -1]
    ans = []
    for i in range(q):
        l, r = map(int, input().split(" "))
        if l == 1:
            ans.append(a[r-1])
        else:
            ans.append(a[r-1] - a[l-2])
    print(*ans)