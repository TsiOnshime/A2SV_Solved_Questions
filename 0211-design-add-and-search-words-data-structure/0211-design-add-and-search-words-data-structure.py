class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def searchChar(self, word,i, curr):
        
        while i < len(word):
            c = word[i]
            if c == ".":
                for keys, vals in curr.children.items():
                    if self.searchChar(word,i+1,vals):
                        return True
                else:
                    return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
            i += 1

        return curr.endOfWord

    def search(self, word: str) -> bool:
        curr = self.root
        i = 0
        return self.searchChar(word, i, curr)
        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna