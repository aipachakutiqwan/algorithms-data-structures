'''
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.
'''

from typing import List

class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Time Complexity: O(NlogN), where N is the length of people.
        Space Complexity: O(logN).
        '''

        sorted_people = sorted(people)
        boats = 0
        i = 0
        j = len(sorted_people)-1

        while i < j:

            if sorted_people[i] + sorted_people[j] <=limit:
                boats+=1
                i+=1
                j-=1
            else:
                boats+=1
                j-=1
        
        if i==j:
            boats+=1
        return boats            
            

if __name__ == "__main__":
    print("Welcome to Boats to Save People Problem")
    SOL = Solution()
    people = [1,2] 
    limit = 3
    assert SOL.numRescueBoats(people, limit) == 1

    people = [3,2,2,1]
    limit = 3
    assert SOL.numRescueBoats(people, limit) == 3

    people = [3,5,3,4]
    limit = 5
    assert SOL.numRescueBoats(people, limit) == 4








        