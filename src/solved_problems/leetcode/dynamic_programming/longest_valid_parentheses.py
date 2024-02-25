'''
Given a string containing just the characters '(' and ')', 
return the length of the longest valid (well-formed) parentheses substring.
'''
from collections import deque

class Solution:

    def longestValidParentheses_dynamic_programming(self, s: str) -> int:
        # dp array where i-th element represents the length of the longest valid substring ending at i-th index.
        # We initialize the complete dp array with 0's.
        dp = [0]*len(s)
        max_value = 0
        # Start from position 1
        for i in range(1, len(s)): 
            # Now, it's obvious that the valid substrings must end with ‘)’. 
            # This further leads to the conclusion that the substrings ending with ‘(’ will always contain '0' at their corresponding dp indices. 
            # Thus, we update the dp array only when ‘)’ is encountered.
            if s[i] == ')':
                # So because the ending "()" portion is a valid substring 
                # anyhow and leads to an increment of 2 in the length of the just previous valid substring's length.
                if s[i-1] == '(':
                    # validate i>=2 to do not go outside the array
                    temp = dp[i-2] if i>=2 else 0
                    dp[i]= temp + 2
                else:
                    #  0      1       2      3      4      5      6      7      8      9      10     
                    #         (       (      (      (      (      )      )      )       )      )
                    #     i-dp[i-1]-1 ................................................. i-i    i
                    # Let call substring (sub_s) from index 2 to 9 that was already calculated in dp[i-1].
                    # Validate i-dp[i-1] to do not go outside of the array
                    # if s[i-dp[i-1]-1] == '(' there is the possibility to increase in 2 elements the dp[i]
                    # The dp[i] will be calculated as the sum of 3 elements:
                    # 1. The length of the valid substring just before the term  "(  sub_s  )".
                    # 2. The lenght of th sub_s
                    # 3. Add 2 which corresponds to "(" and ")" elements
                    if  i-dp[i-1]> 0 and s[i-dp[i-1]-1] == '(':
                        # validate i-dp[i-1] need to be at least 2 to do not go outside of the array
                        temp = dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0
                        dp[i] =  dp[i-1] + temp + 2
                max_value = max(max_value, dp[i])
        return max_value

    def longestValidParentheses_stack(self, s: str) -> int:
        stack = deque()
        stack.append(-1)
        max_value = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    last_element = stack[-1]
                    len_subarray = i - last_element
                    max_value = max(max_value, len_subarray)
        
        return max_value


if __name__ == "__main__":
    print(f'Welcome to longest valid parentheses problem')
    SOL = Solution()
    s = "(()"
    assert SOL.longestValidParentheses_dynamic_programming(s) == 2
    assert SOL.longestValidParentheses_stack(s) == 2
    s = ")()())"
    assert SOL.longestValidParentheses_dynamic_programming(s) == 4
    assert SOL.longestValidParentheses_stack(s) == 4
    s = ""
    assert SOL.longestValidParentheses_dynamic_programming(s) == 0
    assert SOL.longestValidParentheses_stack(s) == 0