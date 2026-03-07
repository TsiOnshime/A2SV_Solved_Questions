t = int(input())

for _ in range(t):
    

    n = int(input())
    num1 = list(map(int, input().split(' ')))   
    
    m = int(input())
    num2 = list(map(int, input().split(' ')))  
    
    
    for i in range(1,len(num1)):
        num1[i] += num1[i - 1]
    
    for i in range(1, len(num2)):
        num2[i] += num2[i - 1]
    
    if max(num1) < 0 and max(num2) >= 0:
        print(max(num2))
    elif max(num2) < 0 and max(num1) >= 0: 
        print(max(num1))
    elif max(num1) < 0 and max(num2) < 0:
        print(0)
    else:
        print(max(num1) + max(num2))
