class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))






    """
            Time Complexity = O(n^2)
            Space Complexity = O(1)


            Say you have an array for which the ith element is the price of a given stock on day i.
            If you were only permitted to complete at most one transaction (i.e., buy one and sell one
            share of the stock), design an algorithm to find the maximum profit.
            Note that you cannot sell a stock before you buy one.

            Example:
            Input: [7,1,5,3,6,4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                         Not 7-1 = 6, as selling price needs to be larger than buying price.

            float("inf") -
            It acts as an unbounded upper value for comparison. This is useful for finding lowest values for something. 
    """
