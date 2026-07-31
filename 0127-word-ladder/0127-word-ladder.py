class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # all words have the same length

        # map pattern with list of words that satisfy that pattern
        adj_list = defaultdict(list)
        n = len(beginWord)
        wordList.append(beginWord)

        for i in range(len(wordList)):
            for j in range(n):
                pat = wordList[i][:j] + "*" + wordList[i][j + 1:]
                adj_list[pat].append(wordList[i])

        
        queue = deque()
        visited = set()

        queue.append([beginWord, 1])
        visited.add(beginWord)

        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist 
            for i in range(n):
                pat = word[:i] + "*" + word[i + 1:]
                for neigh in adj_list[pat]:
                    if neigh not in visited:
                        queue.append([neigh, dist + 1])
                        visited.add(neigh)
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna