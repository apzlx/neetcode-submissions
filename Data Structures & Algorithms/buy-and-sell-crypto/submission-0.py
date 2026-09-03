class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high
        # 0 if it's a decreasing array
        # go through left to right, stack, if the price of the day < price of the day before, we buy on that day, if price of the day> the current lowest price, we save a maxProfit

        minPrice = 101
        maxProfit = 0

        for p in prices:
            if p < minPrice:
                minPrice = p
            else:
                maxProfit = max(maxProfit, p-minPrice)

        return maxProfit