'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then 
mapped back into letters using the reverse of the mapping above 
(there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be 
mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
'''

class Solution:

    def numDecodings_memoization(self, s: str) -> int:
        '''
        Solved with memoization
        Time and space complexity: O(n)
        '''
        memo = {}
        def recursion(s, index):
            # If you reach the end to the string,
            # that means there is one way to form the decoded characters
            if index == len(s):
                return 1
            # If the string starts with a zero, it can't be decoded
            if s[index] == '0':
                return 0
            if index == len(s)-1:
                return 1

            if index in memo:
                # It was calculated previously return the value directly
                return memo[index]
            else:
                # obtain ways adding one element.
                result = recursion(s, index+1)
                # obtain ways adding two elements.
                if int(s[index:index+2]) <= 26:
                    # sum the 1 and 2 ways
                    result += recursion(s, index+2)
                memo[index] = result
                return result
            
        return recursion(s, 0)
    
    def numDecodings_dynamic_programming(self, s: str) -> int:
        '''
        Solved with Dynamic Programming.
        Time and space complexity: O(n)
        '''
        
        # If len s equal 0, there is not way to decode
        if len(s)== 0:
            return 0
        # dp table will contain dp[0] initialization 
        dp = [0]*(len(s)+1)
        dp[0] = 1

        # Ways to decode a string of size 1 is 1. Unless the string is '0'.
        # '0' doesn't have a single digit decode.
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1

        # pos means (pos-1) character in s since dp has len(s)+1 elements
        for pos in range(2, len(dp)):
            # Check if successful single digit decode is possible.
            # if it is zero, decode is not possible, zero has not decoding number.
            if s[pos-1] != '0':
                dp[pos] += dp[pos-1]
            # Check if successful two digit decode is possible.
            # Verify that the 2 elements characters are able to form a decoded element between [10, 26]
            if 10 <= int(s[pos-2:pos]) <=26:
                dp[pos] += dp[pos-2]
            
        # Once we reach the end of the dp table we obtained the decoded ways.
        return dp[-1]
        
if __name__ == "__main__":
    print(f'Welcome to decode ways problem')

    SOL = Solution()
    s = "12"
    assert SOL.numDecodings_dynamic_programming(s) == 2
    s = "226"
    assert SOL.numDecodings_dynamic_programming(s) == 3
    s = "06"
    assert SOL.numDecodings_dynamic_programming(s) == 0

    s = "12"
    assert SOL.numDecodings_memoization(s) == 2
    s = "226"
    assert SOL.numDecodings_memoization(s) == 3
    s = "06"
    assert SOL.numDecodings_memoization(s) == 0






        

