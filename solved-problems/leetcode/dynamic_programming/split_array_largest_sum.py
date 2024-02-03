
'''
Given an integer array nums and an integer m, 
split nums into m non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.
'''

import itertools
from typing import List

class Solution:
    

    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        Here N is the length of the array and M is the number of subarrays allowed.
        Time complexity: O(Nˆ2*M)
        Each state is defined by the values currIndex and subarrayCount. 
        As such, there are N*M possible states, and we must visit almost every state in order to solve the original problem. 
        Each state (subproblem) requires O(N) time because we have a for loop from currIndex to N - subarrayCount. 

        Space complexity: O(N*M)
        The memoization results are stored in the table memory with size N*M.
        Also, stack space in the recursion is equal to the maximum number of active functions. 
        The maximum number of active functions can be equal to M as we only make a recursive call 
        when splitting the array and we do not make a recursive call when there is only 1 subarray remaining. 
        Hence, the space complexity is equal to O(N*M).
        '''
        n =  len(nums)
        # Sum array of nums with first element 0
        prefix_sum = [0] + list(itertools.accumulate(nums))
        # Memory dictionary to store results of min_largest_split_sum already computed
        memory = {}
        
        def get_min_largest_split_sum(curr_index, subarrray_count):
            
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarrray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]
    
            # Otherwise, use the recurrence function to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            
            minimum_largest_split_sum = prefix_sum[n] # maximun possible sum is the sum of all array elements.

            for i in range(curr_index, n - subarrray_count+1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i+1] - prefix_sum[curr_index]

                # Verify in the memory dictionary if there is already a min_largest_split_sum
                # calculation for (i+1, subarrray_count -1)
                min_largest_split_sum = None
                if (i+1, subarrray_count -1) in memory:
                    min_largest_split_sum = memory[(i+1, subarrray_count -1)]
                else:
                    min_largest_split_sum = get_min_largest_split_sum(i+1, subarrray_count -1)
                    memory[(i+1, subarrray_count -1)] = min_largest_split_sum

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum, min_largest_split_sum)

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                # Once firstSplitSum is larger than minimumLargestSplitSum 
                # it is impossible for us to find a better minimumLargestSplitSum because 
                # firstSplitSum will only continue to increase (because all numbers are non-negative) 
                if first_split_sum >= minimum_largest_split_sum:
                    break
            
            return minimum_largest_split_sum


        return get_min_largest_split_sum(0, m)

        

if __name__ == "__main__":

    print(f'Welcome to Split Array Largest Sum')
    SOL = Solution()
    nums = [7,2,5,10,8] 
    m = 2
    #There are four ways to split nums into two subarrays.
    #The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
    assert SOL.splitArray(nums, m) == 18 

    nums = [1,2,3,4,5]
    m = 2
    # There are four ways to split nums into two subarrays.
    # The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
    assert SOL.splitArray(nums, m) == 9







        