from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0

        while i < len(words):
            length = 0
            line = []
            min_space = 0
            last_element = False

            for j in range(i, len(words)):
                if length + len(words[j]) + min_space <= maxWidth:
                    length += len(words[j])
                    line.append(words[j])
                    min_space += 1
                    if j == len(words) - 1:
                        last_element = True
                else:
                    break

            spaces = maxWidth - len("".join(line))

            if len(line) == 1:
                lines.append(line[0] + " " * spaces)

            else:

                # last line
                if last_element:

                    spaces -= (len(line) - 1)

                    justified = []

                    for k in range(len(line)):
                        justified.append(line[k])

                        if k != len(line) - 1:
                            justified.append(" ")
                        else:
                            justified.append(" " * spaces)

                # normal line
                else:

                    extra = spaces % (len(line) - 1)
                    spaces //= (len(line) - 1)

                    justified = []

                    for k in range(len(line)):
                        justified.append(line[k])

                        if k != len(line) - 1:
                            justified.append(" " * spaces)

                            if extra > 0:
                                justified.append(" ")
                                extra -= 1

                lines.append("".join(justified))

            i += len(line)

        return lines

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna