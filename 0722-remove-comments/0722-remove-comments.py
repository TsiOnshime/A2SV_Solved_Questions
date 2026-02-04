class Solution:
    def removeComments(self, source: List[str]) -> List[str]:

        result = []
        in_block = False
        new_line = ""

        for line in source:
            i = 0
            if not in_block:
                new_line = ""  # start fresh if not in block
            while i < len(line):
                if in_block:
                    # look for end of block comment
                    if line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    # check for start of block comment
                    if line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    # check for single-line comment
                    elif line[i:i+2] == "//":
                        break  # ignore rest of line
                    else:
                        new_line += line[i]
                        i += 1
            # add line to result if non-empty and not inside a block
            if new_line and not in_block:
                result.append(new_line)

        return result


                    
