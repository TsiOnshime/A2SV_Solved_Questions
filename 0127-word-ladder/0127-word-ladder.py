class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        wordList.append(beginWord)
        for i in range(len(wordList)):
            for j in range(len(beginWord)):
                word = wordList[i]
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        visited = set()
        queue = deque()
        queue.append([beginWord, 1])
        visited.add(beginWord)
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            neighbors = []
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for k in adj[pattern]:
                    if k == word: 
                        continue
                    neighbors.append(k)
            for neigh in neighbors:
                if neigh not in visited:
                    queue.append([neigh, dist + 1])
                    visited.add(neigh)

        return 0
