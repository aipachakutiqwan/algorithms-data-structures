'''
An attendance record for a student can be represented as a string where each character signifies 
whether the student was absent, late, or present on that day. 
The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of 
length n that make a student eligible for an attendance award. 
The answer may be very large, so return it modulo 109 + 7.
'''


class Solution:

    def eligible_combinations(self, n, total_absences, consecutive_lates, memo, MOD):
        # if the below condition arrives does not have sense to continue exploring.
        if total_absences>= 2 or consecutive_lates >= 3:
            return 0
        # if we explore all the size means we arrived to form a valid string
        if n == 0:
            return 1
        # Return result from memory without calculating it.
        if memo[n][total_absences][consecutive_lates]!= None:
            return memo[n][total_absences][consecutive_lates]
        # For every step there are 3 options (choose present, absent and late), 
        # it is required to add the result from all options.
        count = 0
        count = self.eligible_combinations(n - 1, total_absences, 0, memo, MOD) % MOD  # choose P
        count += self.eligible_combinations(n - 1, total_absences+1, 0, memo, MOD) % MOD # choose A
        count += self.eligible_combinations(n - 1, total_absences, consecutive_lates+1, memo, MOD) % MOD # choose L
        memo[n][total_absences][consecutive_lates] = count
        return count

        
    def checkRecord(self, n: int) -> int:
        '''
        Solved using Top-Down Dynamic Programming with Memoization.
        Time complexity: O(n)
        Our recursive function will only evaluate n*2*3 unique sub-problems due to memorization.
        So, this approach will take O(6⋅n)=O(n) time.
        Space complexity: O(n)
        We initialized an additional array memo of size n*2*3 that takes O(n) space.
        The recursive call stack will also take O(n) space in the worst-case.
        So, this approach will take O(6*n + n)=O(n) space.

        '''
        MOD = 1000000007
        memo = [[[None] * 3 for _ in range(2)] for _ in range(n + 1)]
        return self.eligible_combinations(n, 0, 0, memo, MOD) % MOD


if __name__ == "__main__":
    print('Welcome to Student Attendance Record II problem')
    SOL = Solution()
    n = 2
    assert SOL.checkRecord(n) == 8
    n = 1
    assert SOL.checkRecord(n) == 3
    n = 10101
    assert SOL.checkRecord(n) == 183236316
