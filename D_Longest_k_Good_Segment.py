from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split(" "))

nums = list(map(int, input().split(" ")))


res = 0
count = defaultdict(int)
l = 0 
for r in range(n):
    count[nums[r]] += 1
    while len(count) > k:
        count[nums[l]] -= 1
        if count[nums[l]] == 0:
            del count[nums[l]]
        l += 1
    if r - l + 1 > res:
        res = max(res, r - l + 1)
        right = r
        left = l
        


print(left + 1,right + 1)
