class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0,1
        TotalP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                TotalP = TotalP + profit
            l += 1
            r += 1
        return TotalP

        # max_profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i -1]:
        #         max_profit += prices[i] - prices[i - 1]
        # return max_profit
        
        