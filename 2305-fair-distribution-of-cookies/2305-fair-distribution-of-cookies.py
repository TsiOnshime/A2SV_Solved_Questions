class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        min_unfairness = float('inf')
        children = [0] * k
        n = len(cookies)

        def distribution(index):
            nonlocal min_unfairness

            if index == n:
                min_unfairness = min(min_unfairness, max(children))
                return

            if max(children) >= min_unfairness:
                return

            for i in range(k):
                children[i] += cookies[index]
                distribution(index + 1)
                children[i] -= cookies[index]

        distribution(0)
        return min_unfairness