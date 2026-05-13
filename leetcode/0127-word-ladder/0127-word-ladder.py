class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        n = len(beginWord)
        adj = defaultdict(set)
        queue = deque()
        visited = set()

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(n):
                pat = word[:j] + "*" + word[j + 1:]
                adj[pat].add(word)

        queue.append([beginWord, 1])
        visited.add(beginWord)
        while queue:
            node, dist = queue.popleft()
            if node == endWord:
                return dist
            for j in range(n):
                pat = node[:j] + "*" + node[j + 1:]
                for neigh in adj[pat]:
                    if neigh not in visited:
                        queue.append([neigh, dist + 1])
                        visited.add(neigh)

        return 0




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna