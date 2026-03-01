
t = int(input())

for _ in range(t):
    n, x, k = list(map(int, input().split(" ")))
    s = input(" ")
    
    count = 0
    j = 0
    first_loop = True
    cycle = float('inf')
    for i in range(k + 1):
        if x == 0:
            if first_loop:
                remaining_time = k - i 
                first_loop = False
                idx = i    
            else:
                cycle = i - idx
                break
            j = 0
            
                
        if (j == len(s)) and x != 0:
            break
        
        
        if s[j] == "L": 
            x -= 1
        else: 
            x += 1
        j += 1
        


    if not first_loop and cycle == float("inf"):
        print(1)
    elif first_loop:
        print(0)
    else:
        print(1 + (remaining_time // cycle))
        
    
        
        
        



