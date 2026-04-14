class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l => buying price
        # r => selling price
        # if the selling price is less than or equal to the buying price set the buying price to the selling price and look for a better selling price

        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l = r
            else:
                maxP = max(maxP, profit)

        return maxP


        