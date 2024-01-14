'''
You have n dice, and each dice has k faces numbered from 1 to k.
Given three integers n, k, and target, 
return the number of possible ways (out of the kˆn total ways) to roll the dice, 
so the sum of the face-up numbers equals target. 
Since the answer may be too large, return it modulo 109 + 7.
'''


class Solution:
    
    def calculate_ways(self, memory_ways, dice_index, n, curr_sum, target, k, modulo):
        
        # If all the n dice are traversed, the sum must be equal to target for valid combination
        if dice_index == n:
            return 1 if curr_sum == target else 0
        
        # We have already calculated the answer in the DP table so no need to go into recursion.
        if memory_ways[dice_index][curr_sum] != None:
            return memory_ways[dice_index][curr_sum]
 
        ways = 0
        # Iterate over the possible face value for current dice.
        # min(k, target - curr_sum) since it is required to calculate ways only for the remaining quantity to arrive target,
        # it is not required to calculate the ways for values more than remaining quantity.
        # i start from 1 since face of the dice will always start with 1.
        for i in range(1, min(k, target - curr_sum) + 1):
            # Ways obtained applying the module problem requirement to reduce computations.
            ways = (ways + self.calculate_ways(memory_ways, dice_index+1, n, 
                                               curr_sum + i, target,
                                               k, modulo)) % modulo
                   
        memory_ways[dice_index][curr_sum] = ways
        # the result of the problem will be always in the position memory_ways[0][0] 
        return memory_ways[dice_index][curr_sum] 
            
                
        
    
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        '''
        Problem solved using Dynamic programming (store partial ways matrix with indexes: dice_index and curr_sum)
        
        Here, N is the number of dice, K is the number of faces each dice have, and T is the target value.

        Time complexity: O(N*T*K)
        Each state is defined by the diceIndex and the currSum. Hence, there will be 
        N*T states, and in the worst, we must visit most of the states to solve the original problem. 
        Each recursive call will require O(K) time as we iterate over the possible values from 1 to K. 
        Therefore, the total time required will be equal to O(N*T*K).
        
        Space complexity:
        The memoization results are stored in the table memo with size N*T. 
        Also, stack space in the recursion is equal to the maximum number of active functions. 
        The maximum number of active functions will be at most N, i.e., 
        one function call for every die. Hence, the space complexity is O(N*T).
        '''
        
        # Modulo is part of the problem requirement for avoid large numbers processing
        modulo = 1000000007
        memory_ways = []
        
        # Create ways memory table for store the calculation of the ways (this is the DP table)
        # Memory table has (n-1) * (target) dimensions. 
        # (n-1) since start from 0 and the last index calculation is not stored in the table.
        # (target) since it is required to store until the last target number.
        for f in range(n):
            col = []
            for c in range(target+1):
                col.append(None)
            memory_ways.append(col)
        # dice_index start from 0, dice_index is the number of dice that is being calculated.
        # curr_sum is 0 since still there is not dice calculated.
        return self.calculate_ways(memory_ways, 0, n, 0, target, k, modulo)

if __name__ == "__main__":
    print(f'Welcome to number of dice rolls with target sum Problem')
    SOL = Solution()
    n = 1
    k = 6
    target = 3
    assert SOL.numRollsToTarget(n, k, target) == 1
    n = 2
    k = 6
    target = 7
    assert SOL.numRollsToTarget(n, k, target) == 6
    n = 30
    k = 30
    target = 500
    assert SOL.numRollsToTarget(n, k, target) == 222616187


        
        