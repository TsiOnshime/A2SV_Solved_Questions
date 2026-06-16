class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1 -> Buy
        frontBuy = frontNotBuy = 0


        for i in range(len(prices) - 1, -1, -1):

            currBuy = max(-prices[i] + frontNotBuy, frontBuy)

            currNotBuy = max(prices[i] + frontBuy, frontNotBuy)
                
            frontBuy = currBuy
            frontNotBuy = currNotBuy

        return frontBuy
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna