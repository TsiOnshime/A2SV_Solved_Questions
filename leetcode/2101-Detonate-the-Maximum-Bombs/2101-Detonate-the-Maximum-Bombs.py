class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        # make the graph that has bomb idx : [detonated bombs indexes]
        graph = defaultdict(list)
        _max = 1

        for i in range(len(bombs)):
            x, y, r = bombs[i]
            for j in range(len(bombs)):
                a, b, c = bombs[j]
                if i == j:
                    continue
                if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
                    graph[i].append(j)

        def dfs(start):
            stack = [start]
            _max = 0
            visited = set()

            while stack:
                bomb = stack.pop()
                if bomb in visited:
                    continue
                _max += 1
                visited.add(bomb)
                for b in graph[bomb]:
                    if b not in visited:
                        stack.append(b)

            return _max


        for i in range(len(bombs)):
            _max = max(_max, dfs(i))
        
        return _max