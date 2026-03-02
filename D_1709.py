t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    b = list(map(int, input().split(" ")))
    
    operations = []
    count = 0 
    
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            count += 1
            operations.append(f"3 {i+1}")
        
    for i in range(len(a)):
        swapped = False
        for j in range(0, len(a) - i - 1):
            if a[j+1] < a[j]:
                count += 1
                operations.append(f"1 {j+1}")      
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    
    for i in range(len(b)):
        swapped = False
        for j in range(0, len(b) - i - 1):
            if b[j+1] < b[j]:
                count += 1
                operations.append(f"2 {j+1}")
                b[j], b[j+1] = b[j+1], b[j]
                swapped = True
        if not swapped:
            break
        

        
    print(count)
    for j in operations:
        print(j)


    
        
