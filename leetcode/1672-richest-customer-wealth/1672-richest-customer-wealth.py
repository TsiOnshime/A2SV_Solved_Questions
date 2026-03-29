class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        _max = 0

        rows = len(accounts)
        cols = len(accounts[0])

        for i in range(rows):
            _sum = 0
            for j in range(cols):
                _sum += accounts[i][j]
            _max = max(_max, _sum)

        return _max