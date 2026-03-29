class Solution:
    def toLowerCase(self, s: str) -> str:
        s_list = [""] * len(s)

        for i in range(len(s)):
            s_list[i] = s[i].lower()
        return ("").join(s_list)
            