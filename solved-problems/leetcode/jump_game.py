"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
"""

class Solution:

    def backtracking_can_jump(self, nums, memo, position):
        if memo[position]!=0:
            return True if memo[position]==1 else False
        
        jump_until = min(position + nums[position], len(nums)-1)
        for i in range(position+1, jump_until+1):
            if self.backtracking_can_jump(nums, memo, i):
                memo[position] = 1
                return True

        memo[position] = 2

        return False
        

    def canJump(self, nums: list[int]) -> bool:

        n = len(nums)
        memo = [0]*n # 0: UNK, 1:GOOD, 2:BAD
        memo[n-1] = 1
        # first approach: DP 
        #return self.backtracking_can_jump(nums, memo, position=0)

        # second approach: DP botton-up

        for i in range(len(nums)-2, -1, -1):
            jump_until = min(i + nums[i], len(nums)-1)
            for j in range(i+1, jump_until+1):
                if memo[j]==1:
                    memo[i]=1
                    break
        return True if memo[0]==1 else False


if __name__ == "__main__":
    print(f'Problem Jump Game')
    Solution = Solution()
    test1 = Solution.canJump(nums = [2,3,1,1,4])
    test2 = Solution.canJump(nums = [3,2,1,0,4])
    assert test1 == True
    assert test2 == False





        

        