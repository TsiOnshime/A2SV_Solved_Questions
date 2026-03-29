class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # freq = [0] * 26

        # offset = ord('a')
        # for i in sentence:
        #     freq[ord(i) - offset] += 1
        # if 0 not in freq:
        #     return True
        # return False

        count = Counter(sentence)
        if len(count) == 26:
            return True
        return False
