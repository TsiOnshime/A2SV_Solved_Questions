class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        min_unfairness = float('inf')
        n = len(cookies)
        children = [0] * k

        def solve():
            nonlocal min_unfairness
            search(0)
            return min_unfairness


        def is_valid_state(i):
            nonlocal min_unfairness
            if i == n or max(children) >= min_unfairness:
                return True

        def search(i):
            nonlocal min_unfairness

            if is_valid_state(i):
                min_unfairness = min(min_unfairness, max(children))
                return
            
            for j in range(len(children)):
                children[j] += cookies[i]
                search(i + 1)
                children[j] -= cookies[i]
        return solve()
        