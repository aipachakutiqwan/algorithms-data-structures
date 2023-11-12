
'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".
'''

from collections import Counter

class Solution:

    def sliding_windows(self, s, t):
        '''
        Time Complexity: O(|S| + |T|) where |S| and |T| represent the lengths of strings s and t. |T| in the creation of the counter for t.
        In the worst case we might end up visiting every element of string s twice, once by left pointer and once by right pointer.

        Space Complexity: O(|S| + |T|). |S| when the window size is equal to the entire string s. |T| when t has all unique characters.
        '''
                   
        dict_t = {}
        desired = 0
        # create a counter dictionary for the t string
        for character in t:
            if dict_t.get(character):
                dict_t[character]+=1
            else:
                dict_t[character]=1
                desired+=1
        
        n = len(s)
        formed = 0
        left = 0
        right = 0
        dict_windows = {} # store all the characters in the sliding window
        answer = float('inf'), None, None
        # use sliding window to obtain the shorted string containing the characters in 't'
        while right < n:
            character_right = s[right]
            dict_windows[character_right] = dict_windows.get(character_right, 0) + 1
            # formed will indicate if the sliding window contains the elements of t
            if character_right in dict_t and dict_windows[character_right] == dict_t[character_right]:
                formed +=1
            while left <= right and  formed == desired:
                character_left = s[left]
                # update shortest string if lenght is less than previous found
                if right - left + 1 < answer[0]:
                    answer = right - left + 1, left, right
                dict_windows[character_left] -= 1
                if character_left in dict_t and dict_windows[character_left] < dict_t[character_left]:
                    formed -=1
                left+=1
            right+=1

        if answer[0] == float('inf'):
            return ""
        else:
            return s[answer[1]:answer[2]+1]
    
    def optimized_sliding_windows(self, s, t):
        '''
        Time Complexity : O(|S| + |T|). The complexity is same as the previous approach but in certain cases where |filtered_s| <<< |S|, 
        the complexity would reduce because the number of iterations would be
        2*|filtered_s| (worst case while loop filtered_s) + |S| (creation filtered_s) + |T| (creation counter t).

        Space Complexity : O(|S| + |T|).

        '''
        
        dict_t = {}
        desired = 0
        # create a counter dictionary for the t string
        for character in t:
            if dict_t.get(character):
                dict_t[character]+=1
            else:
                dict_t[character]=1
                desired+=1

        # Optimization: create a filtered_s array containing only existing elements in t 
        filtered_s = []
        for position, character in enumerate(s):
            if character in dict_t:
                filtered_s.append((position, character))
        
        n = len(filtered_s)
        formed = 0
        left = 0
        right = 0
        dict_windows = {} # store all the characters in the sliding window
        answer = float('inf'), None, None
        # use sliding window to obtain the shorted string containing the characters in 't'
        while right < n:
            character_right = filtered_s[right][1]
            dict_windows[character_right] = dict_windows.get(character_right, 0) + 1
            # formed will indicate if the sliding window contains the elements of t
            if character_right in dict_t and dict_windows[character_right] == dict_t[character_right]:
                formed +=1
            while left <= right and  formed == desired:
                character_left = filtered_s[left][1]
                # update shortest string if lenght is less than previous found, consider filtered_s
                start = filtered_s[left][0]
                end = filtered_s[right][0]
                if end - start + 1 < answer[0]:
                    answer = end - start + 1, start, end
                dict_windows[character_left] -= 1
                if character_left in dict_t and dict_windows[character_left] < dict_t[character_left]:
                    formed -=1
                left+=1
            right+=1

        if answer[0] == float('inf'):
            return ""
        else:
            return s[answer[1]:answer[2]+1]



    def minWindow(self, s: str, t: str) -> str:
        #Approach 1
        #return self.sliding_windows(s,t)
        #Approach 2
        return self.optimized_sliding_windows(s,t )




if __name__ == "__main__":
    print(f'Problem minumum windows substring')
    SOL = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    assert SOL.optimized_sliding_windows(s, t) == "BANC"

    s = "a"
    t = "a"
    assert SOL.optimized_sliding_windows(s, t) == "a"

    s = "a"
    t = "aa"
    assert SOL.optimized_sliding_windows(s, t) == ""

