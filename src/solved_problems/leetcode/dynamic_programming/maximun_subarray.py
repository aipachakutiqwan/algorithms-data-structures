'''
Given an integer array nums, find the subarray with the largest sum, and return its sum.
The array will contains negative numbers.
'''
from  typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Solved with Dynamic Programming approach, following 2 ideas in mind.
        
        1. At every position we will potentially obtaing the maximun sum.
        2. In a specific position p, the maximun sum will be obtained summing 
           the previous sum (if it not negative) to the current value:
           dp[pos] = max(dp[pos-1], 0) + nums[i]

        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        current_subarray = nums[0]
        max_subarray = nums[0]

        for pos in range(1, len(nums)):
            num = nums[pos]
            # Discard current_subarray with negative values since we are calculating the maximun
            current_subarray = max(current_subarray, 0) + num
            max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray
    


if __name__ == "__main__":

    print(f'Welcome to Maximun Subarray')
    SOL = Solution()
    a = [-2,1,-3,4,-1,2,1,-5,4]
    assert SOL.maxSubArray(a) == 6
    a = [1]
    assert SOL.maxSubArray(a) == 1
    a = [5,4,-1,7,8]
    assert SOL.maxSubArray(a) == 23