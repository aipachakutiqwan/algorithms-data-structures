'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
'''
from  typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Solved using Dynamic Programming.
        Time Complexity: 0(amount*coins)
        Space Complexity: 0(amount), used to storage DP table.
        '''
    
        # DP table will contain the minimun coins for partial amounts which goes from 0 to amount.
        # The DP table need to be initialized with a maximun value since we would like to get the minimun,
        # this maximun value it is enough to be the amount + 1
        dp = [amount+1]*(amount+1) 
        # This is a base case, if amount=0, the minimun coins is also 0.
        dp[0] = 0
        # For every partial amount, 
        # calculate the minimun coins considering only coins with values less or equal than the partial amount.
        for partial_amount in range(1, amount+1):
            for coin in coins: 
                # Consider coins <= partial amount.
                if (partial_amount >= coin):
                    dp[partial_amount] = min(dp[partial_amount], dp[partial_amount-coin]+1)
        # if the dp[amount] did not changed, that means there is not way to obtain the amount using the coins
        return -1 if dp[amount] == (amount + 1) else dp[amount]

if __name__ == "__main__":

    print(f'Welcome to Coin Change Problem')
    SOL = Solution()
    coins = [1,2,5]
    amount = 11
    assert SOL.coinChange(coins, amount)==3 # 11 = 5+5+1
    coins = [2]
    amount = 3
    assert SOL.coinChange(coins, amount)==-1 # Non way to obtain 3
    coins = [1]
    amount = 0
    assert SOL.coinChange(coins, amount)==0 # if amount is 0, minimun coins to use 0, base case.
    



