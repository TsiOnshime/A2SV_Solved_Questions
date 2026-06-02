class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers_count = {}
        winners = set()
        losers = set()
        for w, l in matches:
            if l not in losers_count:
                losers_count[l] = 1
            else:
                losers_count[l] += 1
        print(losers_count)
        for w, l in matches:
            if w not in losers_count:
                winners.add(w)

            if losers_count[l] == 1:
                losers.add(l)

        WinnersList = sorted(list(winners))
        LosersList = sorted(list(losers))

        return [WinnersList, LosersList]
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna