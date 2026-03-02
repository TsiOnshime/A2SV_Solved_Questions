n, k = list(map(int, input().split(" ")))

nums = list(map(int, input().split(" ")))

h = len(nums)


total_range = (nums[-1] - nums[0])
difference = [nums[i] - nums[i-1] for i in range(1, n)]
difference.sort(reverse= True)
min_cost = total_range - sum(difference[:k-1])
print(min_cost)

    
