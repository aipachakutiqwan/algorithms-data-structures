
'''
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.
'''

from typing import List

class Solution:
    
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        combination = []
        index = 0
        
        def backtracking(remain, index, combination):
            if remain == 0:
                # deep copy of list
                output.append(list(combination))
                return
            if remain < 0:
                return
            
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                backtracking(remain - candidates[i], i, combination)
                # remove with pop, list[:-1] does not work!
                combination.pop()
                
        backtracking(target, index, combination)
        return output
        
if  __name__ == "__main__":
    print('Welcome to combinationSum')
    SOL = Solution()
    candidates = [2,3,6,7]
    target = 7
    output = SOL.combinationSum(candidates=candidates, target=target)
    assert output==[[2,2,3],[7]]
    candidates = [2,3,5]
    target = 8
    output = SOL.combinationSum(candidates=candidates, target=target)
    assert output==[[2,2,2,2],[2,3,3],[3,5]]
    candidates = [2]
    target = 1
    output = SOL.combinationSum(candidates=candidates, target=target)
    assert output==[]


                
                
            
        
