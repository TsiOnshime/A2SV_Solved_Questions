'''
we get the number of casinos and initial coin
we sort the array based on l

[1,2,2], [2,3,3], [3,10, 10]

we check whether our initial coin is between l and r and whether if it is less than the real value:
    if it is:
        we reassign the value of the initial to that of the real value
    we increment the pointer by 1


'''

t = int(input())

for _ in range(t):
    c, initial = list(map(int, input().split(" ")))
    casinos = []
    
    for i in range(c):
        casino = list(map(int, input().split(" ")))
        
        casinos.append(casino)
    casinos.sort(key = lambda x:x[0])
    
    for cs in casinos:
        l, r, real = cs
        
        if l <= initial <= r and initial < real:
            initial = real
    print(initial)
        
    
    
