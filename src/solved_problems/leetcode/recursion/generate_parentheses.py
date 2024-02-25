"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""

class Solution:
    
    def backtracking(self, cur_string, left_count, right_count, n, answer):

        # if the string is completed
        if len(cur_string) == 2*n :
            answer.append("".join(cur_string))
            return
        # left parenthesis can still be added
        if left_count < n:
            cur_string.append('(')
            self.backtracking(cur_string, left_count + 1, right_count, n, answer)
            cur_string.pop()
        # right parenthesis can be added to math a previous unmatched left parenthesis
        if left_count > right_count:
            cur_string.append(')')
            self.backtracking(cur_string, left_count, right_count + 1, n, answer)
            cur_string.pop()
    
    def keep_candidate_valid(self, n):
        '''
        Time complexity: O(4ˆn/sqrt(n))
        Space complexity: O(n)
        '''
        answer = []
        cur_string = []
        left_count = 0
        right_count = 0
        self.backtracking(cur_string, left_count, right_count, n, answer)
        return answer
        
        
    def generateParenthesis(self, n: int) -> list[str]:
        
        # Approach 1: Backtracking considering only valid string candidate
        return self.keep_candidate_valid(n)
        
        
if __name__ == "__main__":
    SOL = Solution()
    n = 3
    res = SOL.generateParenthesis(n)
    assert res == ["((()))","(()())","(())()","()(())","()()()"]
    n = 1
    res = SOL.generateParenthesis(n)
    assert res == ["()"]


            
        