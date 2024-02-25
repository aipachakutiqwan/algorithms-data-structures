
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
        '''
        Let N be the number of candidates, T be the target value, 
        and M be the minimal value among the candidates.

        Time Complexity: O(Nˆ(T/M + 1))

        - As we illustrated before, the execution of the backtracking is unfolded as a DFS traversal in a n-ary tree.
        The total number of steps during the backtracking would be the number of nodes in the tree.
        - At each node, it takes a constant time to process, except the leaf nodes which could take a linear time to make a copy of combination. 
        So we can say that the time complexity is linear to the number of nodes of the execution tree.
        - Here we provide a loose upper bound on the number of nodes.

            ° First of all, the fan-out of each node would be bounded to N, i.e. the total number of candidates.
            ° The maximal depth of the tree, would be T/M, where we keep on adding the smallest element to the combination.
            ° As we know, the maximal number of nodes in N-ary tree of T/M height would be Nˆ(T/M + 1)

        - Note that, the actual number of nodes in the execution tree would be much smaller than the upper bound, 
        since the fan-out of the nodes are decreasing level by level.

        Space Complexity: O(T/M)

        - We implement the algorithm in recursion, which consumes some additional memory in the function call stack.
        - The number of recursive calls can pile up to T/M, where we keep on adding the smallest element to the combination.
        As a result, the space overhead of the recursion is O(T/M)
        - In addition, we keep a combination of numbers during the execution, which requires at most O(T/M) space as well.
        - To sum up, the total space complexity of the algorithm would be O(T/M)
        - Note that, we did not take into the account the space used to hold the final results for the space complexity.

        '''
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


                
                
            
        
