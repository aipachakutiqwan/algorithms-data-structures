'''
Given an integer array nums of unique elements, 
return all possible subsets (the power set).
The solution set must not contain duplicate subsets. 
Return the solution in any order.
'''

from typing import List

class Solution:
    def backtracking(self, nums, index, subset, subsets):
        if index == len(nums):
            subsets.append(subset[:])
            return
        subset.append(nums[index])
        self.backtracking(nums, index+1, subset, subsets)
        subset.pop()
        self.backtracking(nums, index+1, subset, subsets)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''

        Solved using backtracking approach.

        Time complexity: O(N*2^N) to generate all subsets and then copy them into the output list.
        Space complexity: O(N). We are using O(N) space to maintain subset, 
                          and are modifying subset in-place with backtracking. 
                          Note that for space complexity analysis, 
                          we do not count space that is only used for the purpose of returning output, 
                          so the output array is ignored.
        '''
        subsets = []
        subset = []
        index = 0
        self.backtracking(nums, 0, subset, subsets)
        return subsets

if __name__ == "__main__":
    print(f'Welcome to Subsets creation problem')
    SOL = Solution()
    nums = [1,2,3]
    print(SOL.subsets(nums)) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    nums = [0]
    print(SOL.subsets(nums)) # [[],[0]]
