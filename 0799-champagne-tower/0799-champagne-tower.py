class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return 1 if poured > 0 else 0
        res = [poured]
        for i in range(query_row):
            nxt = [0] * (len(res) + 1)
            for j in range(len(res)):
                overflow = res[j] - 1
                if overflow > 0:
                    nxt[j] += overflow/2
                    nxt[j + 1] += overflow / 2
            if i + 1 == query_row:
                    return float(min(1, nxt[query_glass]))
            res = nxt
            
        return 0
        





        
        





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna