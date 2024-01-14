
'''
Consider all the leaves of a binary tree, from left to right order, 
the values of those leaves form a leaf value sequence.

            3
          /   \
         /     \
        5       1
       / \      /\
      /   \    /  \
      6   2    9   8
         / \
        7   4

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

'''
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from queue import Queue

class Solution:
    
    def preorder(self, root, leafs):
        '''
        Deep first search for traverse the tree storing the leafs values
        '''
        if root:            
            if root.left==None and root.right == None:
                leafs.append(root.val)
            self.preorder(root.left, leafs)
            self.preorder(root.right, leafs)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        DFS for calculate the leaf nodes and comparison of resulting leaf nodes arrays.
        Time complexity: O(T1+T2) where T1 and T2 are the lengths of the given trees.
        Space complexity: O(T1+T2) the space used in storing the leaf values.

        '''
        arr1 = []
        arr2 = []
        self.preorder(root1, arr1)
        self.preorder(root2, arr2)
        print(f'arr1: {arr1}')
        print(f'arr2: {arr2}')
        if len(arr1)!= len(arr2):
            return False
        else:
            for i in range(len(arr1)):
                if arr1[i]!=arr2[i]:
                    return False
        return True

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
    print(f'Welcome to leaf similar trees')
    SOL = Solution()
    arr1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    arr2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    root1 = SOL.create_tree(arr1)
    root2 = SOL.create_tree(arr2)
    assert SOL.leafSimilar(root1, root2) == True

    arr3 = [1,2,3]
    arr4 = [1,3,2]
    root3 = SOL.create_tree(arr3)
    root4 = SOL.create_tree(arr4)
    assert SOL.leafSimilar(root3, root4) == False

                    
       