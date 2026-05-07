class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        self._max = -1
        self.res  = set()

        self.dfs(s, 0, [], 0, 0)

        return list(self.res)

    
    def dfs(self, s, i, state, open_count, close_count):
        if i == len(s):
            if open_count == close_count:
                char = "".join(state)
                if len(char) > self._max:
                    self._max = len(state)
                    self.res = {char}

                elif len(char) == self._max:
                    self.res.add(char) 

            return

        char = s[i]

        if char == "(":
            state.append(char)
            self.dfs(s, i + 1, state, open_count + 1, close_count)
            state.pop()
            self.dfs(s, i + 1, state, open_count, close_count)

        elif char == ")":
            self.dfs(s, i + 1, state, open_count, close_count)
            if open_count > close_count:
                state.append(char)
                self.dfs(s, i + 1, state, open_count, close_count + 1)
                state.pop()

        else:
                state.append(char)
                self.dfs(s, i + 1, state, open_count, close_count)
                state.pop()
            
                