'''
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. 
There are n coins in total throughout the whole tree.
In one move, we may choose two adjacent nodes and move one coin from one node to another. 
A move may be from parent to child, or from child to parent.
Return the minimum number of moves required to make every node have exactly one coin.
'''

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from typing import Optional
from queue import Queue

class Solution:

    def dfs(self, current):
        # No coins needs to be exchanged
        if current == None:
            return 0, 0
        # left_coins to the number of coins the left subtree needs to exchange
        left_coins, moves1 = self.dfs(current.left)
        # right_coins to the number of coins the right subtree needs to exchange
        right_coins, moves2  = self.dfs(current.right)
        # number of moves needed to distribuite coins in each of the subtrees
        moves = moves1 + moves2 + abs(left_coins) + abs(right_coins)
        # number of coins the current node has available to exchange with its parent.
        coins_exchange = (current.val - 1) + left_coins + right_coins
        return coins_exchange, moves

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        coins_exchange , moves = self.dfs(root)
        return moves 

    def create_tree(self, arr):
        '''
        Populate tree with array elements using Breath First Search approach .
        '''
        first = arr[0]
        node = TreeNode(first)
        root = node
        count = 1
        q = Queue()
        q.put(node)
        while count < len(arr):
            while q:
                node = q.get()
                if count < len(arr):
                    if arr[count] != None:
                        node.left = TreeNode(arr[count])
                    q.put(node.left)
                    count+=1
                else:
                    break
                if count < len(arr):
                    if arr[count] != None:
                        node.right = TreeNode(arr[count])
                    q.put(node.right)
                    count+=1
                else:
                    break
        return root


if __name__ == "__main__":
    
    print(f'Welcome to Distribute Coins Binary Tree Problem')
    SOL = Solution()
    arr =  [3,0,0]
    root = SOL.create_tree(arr)
    assert SOL.distributeCoins(root) == 2
    arr =  [0,3,0]
    root = SOL.create_tree(arr)
    assert SOL.distributeCoins(root) == 3



        