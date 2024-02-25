'''
Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
'''

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Problem solved using Dynamic Programming approach. 
        max_so_far keeps track of the accumulated product of positive numbers,
        min_so_far is used to handle negative numbers.

        max_so_far is updated taking the maximun among:
        1. current number: it will be picked if the accumulated product has been really bad
           (preceding zero or single negative number)
        2. max_so_far * current number: if the accumulated product has been steadily increasing.
        3. min_so_far * current number: if the current number is negative and the calculation had 
           a single negative number before
        
        min_so_far is updated taking the minimun among the same 3 numbers.

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''

        min_so_far = nums[0]
        max_so_far = nums[0]
        # max_product maintains the maximun product calculation
        max_product = nums[0]

        for pos in range(1, len(nums)):
            current = nums[pos]
            previous_min_so_far = min_so_far # store temporary to use in max_so_far calculation
            min_so_far = min(current, max_so_far*current, min_so_far*current)
            max_so_far = max(current, max_so_far*current, previous_min_so_far*current)
            max_product = max(max_product, max_so_far)
            
        return max_product

if __name__ == "__main__":
    print(f'Welcome to Maximun Product Subarray')
    SOL = Solution()
    nums = [2,3,-2,4]
    assert SOL.maxProduct(nums) == 6
    nums = [-2,0,-1]
    assert SOL.maxProduct(nums) == 0

        