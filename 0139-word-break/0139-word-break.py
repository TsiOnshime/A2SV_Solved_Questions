class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 1:
            return s in wordDict
        queue = deque()
        queue.append(0)
        wordDict = set(wordDict)
        visited = set()
        
        while queue:
            start = queue.popleft()

            if start == len(s):
                return True
            visited.add(start)

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict and end not in visited:
                    queue.append(end)
                    visited.add(end)
        # queue = [0], visited = {}, start = 0, end = 
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna