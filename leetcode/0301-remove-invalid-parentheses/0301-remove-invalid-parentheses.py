class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.max_length = -1

        self.res = set()

        self.dfs(s, 0, [], 0, 0)

        return list(self.res)

    def dfs(self, word, i, state, o_count, c_count):
        if i >= len(word):
            if o_count == c_count:
                if len(state) > self.max_length:
                    self.max_length = len(state)

                    self.res = set()
                    self.res.add("".join(state))
                elif len(state) == self.max_length:
                    self.res.add("".join(state))

            return 

        char = word[i]
        if char == "(":
            state.append(char)
            self.dfs(word, i + 1, state, o_count + 1, c_count)
            state.pop()
            self.dfs(word, i + 1, state, o_count, c_count)
        elif char == ")":
            self.dfs(word, i + 1, state, o_count, c_count)

            if o_count > c_count:
                state.append(char)
                self.dfs(word, i + 1, state, o_count, c_count + 1)
                state.pop()
        else:
            state.append(char)
            self.dfs(word, i + 1, state, o_count, c_count)
            state.pop()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna