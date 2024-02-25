'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.
'''
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        Solved with DP approach.
        Time complexity: 0(nˆ2)
        Space complexity: 0(n)
        '''

        # dp table will contains the maximun lenght for every position i,
        # the maximun lenght for every position will change, depends on the previous values
        dp = [1] * len(nums)
        # this maximun_length variable capture result of the position with the maximun lenght 
        maximun_length = 0
        for i, num in enumerate(nums):
            # Review all the previous elements
            for j in range(0, i):
                # If previous element are less than nums[i], there is a check to do, and update the dp[i]
                # dp[j]+1 is the lenght at position j + 1 (this 1 is if we add the actual position i element)
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            maximun_length = max(maximun_length, dp[i])

        return maximun_length


if __name__ == "__main__":
    print(f'Welcome to Longest Increasing subsequence')
    SOL = Solution()
    nums = [10,9,2,5,3,7,101,18]
    assert SOL.lengthOfLIS(nums) == 4
    nums = [0,1,0,3,2,3]
    assert SOL.lengthOfLIS(nums) == 4
    nums = [7,7,7,7,7,7,7]
    assert SOL.lengthOfLIS(nums) == 1

