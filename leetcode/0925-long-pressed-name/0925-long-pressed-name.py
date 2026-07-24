class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        nameChar = name[i]
        typedChar = typed[j]

        while i < len(name) and j < len(typed):
            if name[i] != typed[j]:
                return False

            nameIdx = i + 1 
            typedIdx = j + 1
            while nameIdx < len(name) and name[nameIdx] == name[i]:
                nameIdx += 1
            while typedIdx < len(typed) and typed[typedIdx] == typed[j]:
                typedIdx += 1
            
            nameCount = nameIdx - i
            typedCount = typedIdx - j
           
            if nameCount > typedCount:
                return False
            
            i = nameIdx
            j = typedIdx
        return i == len(name) and j == len(typed)

# in
# alex

# jt
# aaleex

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna