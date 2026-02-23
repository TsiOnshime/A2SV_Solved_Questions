'''
The answer is always in the middle
if odd return the element at index n/2
1 2 3 4 5
5//2 = 2 so 3 it is

if even return the left most element n/2 - 1
1 2 3 4
4/2 = 2 - 1 so 2 it is

'''
n = int(input())
nums = sorted(list(map(int, input().split(" "))))

if n % 2 != 0:
    idx = n // 2
    print(nums[idx])
else:
    idx = (n // 2) - 1
    print(nums[idx])
