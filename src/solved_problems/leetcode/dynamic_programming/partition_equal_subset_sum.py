'''
Given an integer array nums, 
return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

'''

from typing import List
class Solution:

    def dfs(self, pos, partition_sum, nums, memo):
        # if the partition_sum is zero that means there is a way to obtain the partition sum.    
        if partition_sum == 0:
            return True
        # if sum_target is less than zero, there is not anymore possibility to obtain the partition sum.
        # if pos=0, we covered all the elements of the nums and we did not obtained the partition sum.
        if partition_sum < 0  or pos == 0:
            return False
        # Verify if there is the result in the memo table
        if (pos, partition_sum) in memo:
            return memo[(pos, partition_sum)]
        else:
            # Verify the result of two options: pick the pos-1 element of nums or not pick the pos-1 element of nums
            memo[(pos, partition_sum)] = self.dfs(pos-1, partition_sum - nums[pos-1], nums, memo) or \
                                         self.dfs(pos-1, partition_sum, nums, memo)
            return memo[(pos, partition_sum)]

    def canPartition(self, nums: List[int]) -> bool:
        '''
        Solved using Top Down Dynamic Programming approach (memoization).
        Let n be the number of array elements and m be the subSetSum.

        Time Complexity : O(m⋅n).
        In the worst case where there is no overlapping calculation, 
        the maximum number of entries in the memo would be m⋅n. 
        For each entry, overall we could consider that it takes constant time, 
        i.e. each invocation of dfs() at most emits one entry in the memo.
        The overall computation is proportional to the number of entries in memo. 
        Hence, the overall time complexity is O(m⋅n).

        Space Complexity: O(m⋅n). 
        We are using a 2 dimensional array memo of size (m⋅n) 
        and O(n) space to store the recursive call stack. 
        This gives us the space complexity as O(n) + O(m⋅n) = O(m⋅n)

        '''
        # Memo table will store the partial obtained results to avoid recalculate them.
        # Memo will indexed as (pos, partition_sum)
        memo = {}
        sum_nums = sum(nums) 
        # if sum is even, there is not possibility to split in 2 equal sum subsets
        if sum_nums % 2 != 0:
            return False
        else:
            partition_sum = sum_nums / 2
            # Apply DFS traverse until reach the half of the total sum
            return self.dfs(len(nums)-1, partition_sum, nums, memo)

if __name__ == "__main__":
    print(f'Welcome to Partition Equal Subset Sum')
    SOL = Solution()
    nums = [1,5,11,5]
    assert SOL.canPartition(nums) == True
    nums = [1,2,3,5]
    assert SOL.canPartition(nums) == False
    nums = [1,1,2,2]
    assert SOL.canPartition(nums) == True
    nums = [1,3,4,4]
    assert SOL.canPartition(nums) == False

                



        