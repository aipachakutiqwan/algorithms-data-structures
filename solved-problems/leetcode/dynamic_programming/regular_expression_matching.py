'''

Given an input string s and a pattern p, 
implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', 
there will be a previous valid character to match.
'''
class Solution:

    def recursive(self, s: str, p: str) -> bool:
        '''
        Recursive approach, it is going to timeout.
        This approach is useful to understand how to build the dp solution.
        '''
        if not p:
            return not s
        first_check = bool(s) and p[0] in {s[0], '.'}
        # contraints problem: It is guaranteed for each appearance of the character '*', 
        # there will be a previous valid character to match.
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or 
                    first_check and self.isMatch(s[1:], p))
        else:
            return first_check and self.isMatch(s[1:], p[1:])
            

    def dp(self, s: str, p: str) -> bool:
        '''
        Solved with DP approach, let store partial values in memo table (i,j) indexes where
        i is the partial position of s
        j is the partial position of p
        Applying the same recursive approache but this time storing the partial results.

        Time Complexity: Let T, P be the lengths of the text and the pattern respectively. 
        The work for every call to dp(i, j) for i=0,...,T; j=0,...,P is done once, 
        and it is O(1) work. Hence, the time complexity is O(TP).

        Space Complexity: The only memory we use is the O(TP) boolean entries in our cache. 
        Hence, the space complexity is O(TP).
        
        '''
        memo = {}

        def dynamic_programming(i, j):
            # if there is not more elements in the pattern, verify that the text still contains characters
            if not (j < len(p)):
                return not (i < len(s))
            # return the partial precalculated results
            if (i,j) in memo:
                return memo[(i,j)]
        
            first_check = bool(i<len(s)) and (p[j] in ['.', s[i]])

            if j < (len(p) - 1) and p[j+1] == '*':
                # store partial results
                memo[(i,j)] = dynamic_programming(i, j+2) or ( first_check and dynamic_programming(i+1, j))
                return memo[(i,j)]
            else:
                # store partial results
                memo[(i,j)] = first_check and dynamic_programming(i+1, j+1)
                return memo[(i,j)]

        return dynamic_programming(0, 0)

    def isMatch(self, s: str, p: str) -> bool:

        #return self.recursive(text, pattern)
        return self.dp(s, p)
        

if __name__ == "__main__":
    print(f'Welcome to Regular Expression Matching problem')
    SOL = Solution()
    s = "aa"
    p = "a"
    assert SOL.isMatch(s, p) == False

    s = "aa"
    p = "a*"
    assert SOL.isMatch(s, p) == True

    s = "ab"
    p = ".*"
    assert SOL.isMatch(s, p) == True




