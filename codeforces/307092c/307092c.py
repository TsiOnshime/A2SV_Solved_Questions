n, m = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
#8 7
#1 1 3 3 3 5 8 8
#1 3 3 4 5 5 5

i = j = 0
res = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        x = a[i] 
        count_a = 0
        count_b = 0
        
        while i < n and a[i] == x:
            count_a += 1
            i += 1
        while j < m and b[j] == x:
            count_b += 1
            j += 1
        res += count_a * count_b
print(res)