'''
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

'''

from typing import List

class Solution:

    def dp(self, s, i, memo, wordDict):
        # Negative i values are considered True.
        if i<0:
            return True
        # Return value from memo table if there exist.
        if memo[i]!=None:
            return memo[i]
        # Verify for every element of the wordDict
        for word in wordDict:
            if  s[i-len(word)+1:i+1] == word and self.dp(s, i-len(word), memo, wordDict):
                memo[i] = True
                return True
        # If any word from wordDict accomplished the conditions, set index i as False
        memo[i] = False
        return False
        
                        

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Solved with Dynamic programming approach.
        Given n as the length of s, m as the length of wordDict, 
        and k as the average length of the words in wordDict
        Time Complexity: O(n*m*k)
                         There are n states of dp(i). Because of memoization, 
                         we only calculate each state once. To calculate a state, 
                         we iterate over m words, and for each word perform some substring operations which costs O(k). 
                         Therefore, calculating a state costs O(m⋅k), and we need to calculate O(n) states.
        Space Complexity: O(n)
                         The data structure we use for memoization and the recursion call stack can use up to O(n) space.
                         
        '''
        # memo table is used to store partial results and avoid recalculation
        memo = [None]*len(s)
        for i in range(len(s)):
            memo[i] = self.dp(s, i, memo, wordDict)
        return memo[-1]
        # Alternative call to dp function, without for above for loop  
        # return self.dp(s, len(s)-1, memo, wordDict)
        

if __name__ == "__main__":
    print(f'Welcome to word break problem')
    SOL = Solution()
    s = "leetcode"
    wordDict = ["leet","code"]
    assert SOL.wordBreak(s, wordDict) == True
    s = "applepenapple"
    wordDict = ["apple","pen"]
    assert SOL.wordBreak(s, wordDict) == True
    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    assert SOL.wordBreak(s, wordDict) == False


        