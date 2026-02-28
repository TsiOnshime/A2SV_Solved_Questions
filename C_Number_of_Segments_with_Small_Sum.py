##  Number of Segments with Small Sum

n, max_sum = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))


res = 0
_sum = 0
l = 0
for r in range(n):
    _sum += nums[r]
    while _sum > max_sum:
        _sum -= nums[l]
        l += 1
    res += r - l + 1
    
print(res)
