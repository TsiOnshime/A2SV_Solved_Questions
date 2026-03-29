class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        _max = 0
        for i in sentences:
  
            _max = max(_max, len(i.split(" ")))

        return _max