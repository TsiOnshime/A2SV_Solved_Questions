class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int)

        for w, l in matches:
            loss_count[l] += 1
            loss_count[w] += 0
        
        answer = []
        zero_losses = []
        one_losses = []
        for player, cnt in loss_count.items():
            if cnt == 0:
                zero_losses.append(player)
            elif cnt == 1:
                one_losses.append(player)
        
        zero_losses.sort()
        one_losses.sort()
        answer.append(zero_losses)
        answer.append(one_losses)

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna