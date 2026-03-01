from collections import defaultdict

n, k = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))


count = defaultdict(int)
res = 0
l = 0
for r in range(n):
    count[nums[r]] += 1
    while len(count) > k:
        count[nums[l]] -= 1
        if count[nums[l]] == 0:
            del count[nums[l]]
        l += 1
    res += r - l + 1
    
print(res)

        

