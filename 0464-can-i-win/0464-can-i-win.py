class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if (maxChoosableInteger * (maxChoosableInteger + 1))//2 < desiredTotal:
            return False
        if desiredTotal < 0:
            return True
        cache = {}
        def dfs(used, remaining):
            if used in cache:
                return cache[used]
            for i in range(1, maxChoosableInteger + 1):
                if used & (1 << i):
                    continue
                
                if i >= remaining:
                    cache[used] = True
                    return True
                next_used = used | (1 << i)
                
                if not dfs(next_used, remaining - i):
                    cache[used] = True
                    return True
                
            cache[used] = False
            return False
        return dfs(0, desiredTotal)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna