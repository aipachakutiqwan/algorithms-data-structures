'''
Given a string s, return the longest palindromic substring in s.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Dynamic programming solution for the problem uses a DP table of lenght = len(s).
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
        '''

        n = len(s)
        dp = []
        # dp[i][j] is True if it is a string of only one element
        for i in range(n):
            dp.append([])
            for j in range(n):
                if i==j: 
                    dp[i].append(True)
                else:
                    dp[i].append(False)
                    
        # Tuple to store the longest string indexes 
        longest_indexes = (0,0)
        
        # The problem will be solved comparing all the diff between characters.
        # This step calculate the palindrome check for the diff = 1 (2 consecutive characters)
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                longest_indexes = [i, i+1]

        # The step calculate the palindrome check for diff from 2 to n-1
        for diff in range(2, n):
            for i in range(n-diff):
                j = i + diff
                # if the characters in i and j are the same and if [(i+1), (j-1)] positions create a palindrome
                # Palindrome check for [(i+1), (j-1)] have been checked previusly since the diff is less than the actual.
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    longest_indexes=(i, j)
        i,j = longest_indexes
        
        return s[i:j+1]
    
        
if __name__ == "__main__":
    print(f'Welcome to longest palindromic substring solution')
    SOL = Solution()
    s = "babad"
    assert SOL.longestPalindrome(s)=="bab" or SOL.longestPalindrome(s)=="aba"
    s = "cbbd"
    assert SOL.longestPalindrome(s)=="bb"


                
        