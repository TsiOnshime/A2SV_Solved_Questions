t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    _max = max(a)
    count = 0
    for z in range(n-1,1,-1):
        x = 0
        y = z-1
        
        while x < y:
            if a[x] + a[y] + a[z] > max(_max, a[z] * 2):
                count += y-x
                y -= 1
            else:
                x += 1
    print(count)