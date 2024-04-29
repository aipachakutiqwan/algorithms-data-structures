'''
You are given a 0-indexed integer array nums and a positive integer k.
You can apply the following operation on the array any number of times:
Choose any element of the array and flip a bit in its binary representation. 
Flipping a bit means changing a 0 to 1 or vice versa.
Return the minimum number of operations required to make the bitwise XOR of all elements of the final array equal to k.
Note that you can flip leading zero bits in the binary representation of elements. 
For example, for the number (101) you can flip the fourth bit and obtain (1101).

'''

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        '''
        Solved using bit-wise operations approach.
        '''
        xor_final = 0
        for num in nums:
            xor_final ^= num
        count_changes = 0

        while (xor_final or k):
            if (xor_final % 2 != k % 2):
                count_changes +=1
            xor_final = xor_final // 2
            k = k // 2
            
        return count_changes


if __name__ == "__main__":
    SOL = Solution()
    nums = [2,1,3,4]
    k = 1
    assert SOL.minOperations(nums, k) == 2
    nums = [2,0,2,0] 
    k = 0
    assert SOL.minOperations(nums, k) == 0


        