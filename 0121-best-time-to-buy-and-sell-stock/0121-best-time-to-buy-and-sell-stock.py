class Solution(object):
    def maxProfit(self, prices):
        #TC=O(n) SC=O(1)
        maxProfit = 0
        preMin = prices[0]
        for i in prices:
            maxProfit=max(maxProfit,i-preMin)
            preMin=min(preMin,i)
        return maxProfit


        #TC=O(n^2) SC=O(1)
        # maxProfit = 0
        # for i in range(len(prices)):
        #     profit = 0
        #     for j in range(i+1,len(prices)):
        #         if prices[j]>prices[i]:
        #             profit = max(profit,prices[j]-prices[i])
        #     maxProfit = max(profit,maxProfit)
        # return maxProfit
