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
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
 
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
    
    def dp_top_down(self, nums):
        '''
        Time complexity : O(nˆ2)
        Space complexity : O(2n)=O(n). First n originates from recursion. 
                           Second n comes from the usage of the memo table.
        '''

        n = len(nums)
        memo = [0]*n # 0: UNK, 1:GOOD, 2:BAD
        memo[n-1] = 1
        return self.backtracking_can_jump(nums, memo, position=0)

    def dp_botton_up(self, nums):
        '''
        Time complexity : O(nˆ2)
        Space complexity : O(n)
        '''

        n = len(nums)
        memo = [0]*n # 0: UNK, 1:GOOD, 2:BAD
        memo[n-1] = 1
        for i in range(len(nums)-2, -1, -1):
            jump_until = min(i + nums[i], len(nums)-1)
            for j in range(i+1, jump_until+1):
                if memo[j]==1:
                    memo[i]=1
                    break
        return True if memo[0]==1 else False    

    def greedy(self, nums):
        '''
        Time complexity : O(n). We are doing a single pass through the nums array.
        Space complexity : O(1). We are not using any extra memory.
        '''
        n = len(nums)
        left_most_good_index = n - 1
        for pos in range(n-1, -1, -1):
            if pos + nums[pos] >= left_most_good_index:
                left_most_good_index = pos
        return left_most_good_index == 0

        

    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        memo = [0]*n # 0: UNK, 1:GOOD, 2:BAD
        memo[n-1] = 1
        # first approach: DP Top-down
        #return self.dp_top_down(nums)
        # second approach: DP Botton-up
        #return self.dp_botton_up(nums)
        # third approach: Greedy
        return self.greedy(nums)


if __name__ == "__main__":
    print(f'Problem Jump Game')
    Solution = Solution()
    test1 = Solution.canJump(nums = [2,3,1,1,4])
    test2 = Solution.canJump(nums = [3,2,1,0,4])
    assert test1 == True
    assert test2 == False





        

        