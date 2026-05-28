class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        failed = set()
        wordDict.sort(reverse=True)
        print(wordDict)
        def search(s_idx):
            if s_idx >= len(s):
                return True
            if s_idx in failed:
                return 
            for word in wordDict:
                end = len(word)
                if s[s_idx:s_idx + end] == word:
                    if search(s_idx + end):
                        return True
            failed.add(s_idx)
        if search(0):
            return True
        return False

                



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna