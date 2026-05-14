from collections import deque, defaultdict
class Solution:
    def findSequences(self, beginWord, endWord, wordList):
        node = [beginWord]
        queue = deque()
        queue.append(node)
        visited = set()
        visited.add(beginWord)
        adj = defaultdict(set)
        res = []
        wordList.append(beginWord)
        n, m = len(wordList), len(wordList[0])

        for i in range(n):
            word = wordList[i]
            for j in range(m):
                pattern = word[:j] + "#" + word[j + 1:]
                adj[pattern].add(word)
        
   
        notFound = True
        while queue and notFound:
            n = len(queue)
            mark = set()

            for i in range(n):
                node = queue.popleft()
                word = node[-1]
                
                if word == endWord:
                    res.append(node)
                    notFound = False
                    continue
                for j in range(m):
                    pat = word[:j] + "#" + word[j + 1:]
                    for neigh in adj[pat]:
                        if neigh == word or neigh in visited:
                            continue
                        mark.add(neigh)
                        
                        queue.append(node + [neigh])
                        
            
            visited.update(mark)

        return res

            
                        
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna