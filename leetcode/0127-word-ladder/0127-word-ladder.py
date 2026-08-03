class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        pat_words = defaultdict(list)

        n = len(beginWord)

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(n):
                pattern = word[:j] + "*" + word[j+1:]
                pat_words[pattern].append(word)
        print(pat_words)

        queue = deque()
        queue.append([beginWord, 1])
        visited = set()
        visited.add(beginWord)

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(n):
                pattern = word[:i] + "*" + word[i + 1:]
                for neigh in pat_words[pattern]:
                    if neigh not in visited:
                        queue.append([neigh, dist + 1])
                        visited.add(neigh)
        return 0
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna