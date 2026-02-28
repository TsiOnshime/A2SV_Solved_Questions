
n, min_sum = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))


res = 0
_sum = 0
l = 0
for r in range(n):
    _sum += nums[r]
    while _sum >= min_sum:
        _sum -= nums[l]
        l += 1
    
    res += l
        
print(res)
