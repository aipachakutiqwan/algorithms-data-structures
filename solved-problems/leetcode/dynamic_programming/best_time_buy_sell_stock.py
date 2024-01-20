'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Solved with Dynamic programming approach, consider some ideas.
        1. Every position will potentially get the max profit
        2. At every position verify if selling the stock, 
           it will increase the maximun profit obtained until here. 
           In addition, decide if it is the best moment to buy a stock 
           (has lower prices than in previous steps)
        
        Time complexity: O(n)
        Space complexity: O(1)
        
        '''
        
        max_profit = 0
        buy = prices[0]
        for pos in range(1, len(prices)):
            value_stock = prices[pos]
            max_profit = max(max_profit, value_stock - buy)
            buy = min(buy, value_stock)
        
        return max_profit

if __name__ == "__main__":
    SOL = Solution()
    prices = [7,1,5,3,6,4]
    assert SOL.maxProfit(prices) == 5
    prices = [7,6,4,3,1]
    assert SOL.maxProfit(prices) == 0


                
        
            
        