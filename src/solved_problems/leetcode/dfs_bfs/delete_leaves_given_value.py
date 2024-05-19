
'''
Given a binary tree root and an integer target, delete all the leaf nodes with value target.
Note that once you delete a leaf node with value target, 
if its parent node becomes a leaf node and has the value target, 
it should also be deleted (you need to continue doing that until you cannot).
'''

from typing import Optional
from queue import Queue

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        Solved using DFS approach (post order traversal)
        '''
        if root == None:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None and root.val == target:
            return None
        else:
            return root


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
    print(f'Welcome to Delete leaves with a given value Problem')
    SOL = Solution()
    arr = [1,2,3,2,None,2,4]
    root = SOL.create_tree(arr)
    print(SOL.removeLeafNodes(root, target=2)) # output: [1,None,3,None,4]
    
    arr = [1,3,3,3,2]
    root = SOL.create_tree(arr)
    print(SOL.removeLeafNodes(root, target=3)) # output: [1,3,None,None,2]

    #arr = [1,2,None,2,None,2]
    #root = SOL.create_tree(arr)
    #print(SOL.removeLeafNodes(root, target=2)) # output: [1]

        
        



        
        
        