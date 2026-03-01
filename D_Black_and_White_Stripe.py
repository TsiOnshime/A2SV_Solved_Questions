
from collections import defaultdict
t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    stripe = input(" ")
    
    count = defaultdict(int)
    
    res = float('inf')
    l = 0
    for r in range(n):
        count[stripe[r]] += 1
        
        
        
        while r - l + 1 > k:
            count[stripe[l]] -= 1
            if count[stripe[l]] == 0:
                del count[stripe[l]]
            l += 1
        if r - l + 1 == k:
            res = min(res, count["W"])
            
    print(res)
    
    
    
            
