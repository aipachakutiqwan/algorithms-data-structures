'''
Given the roots of two binary search trees, root1 and root2, 
return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.

Example 1:

        2               1
       / \             / \
      1   4           0   3

            output = True

Example 2:
      
        0                5
       / \              / \
    -10   10           1   7
                      / \
                     0   2
                     
            output = False
'''
from typing import Optional
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    
    def bst(self, root, value):
        
        while root:
            if root.val == value:
                return True
            if value > root.val:
                root = root.right
            else:
                root = root.left
        return False
    
    
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        '''
        Preorder traverse of the root1 looking the (target - node value) in the root 2 using Binary Search Tree traverse.
        Time complexity: O(m * log n), m number elements node root1 and log n is the BST in root2. 
                         Assume that both trees are balanced, the height of root1 and root2 is O(log m) and O(log n), respectively.

        Space complexity: The space complexity of DFS over a binary tree is O(h), where h is the tree's height. 
                          This is because the DFS algorithm uses a call stack to keep track of the nodes it has visited, 
                          and the maximum size of the call stack is proportional to the height of the DFS tree. 
                          Assume that both trees are balanced, then the height of root1 and root2 is O(log m) and O(log n), respectively.
        '''
        if root1:
            value = target -  root1.val
            found = self.bst(root2, value)
            if found:
                return True
            return self.twoSumBSTs(root1.left, root2, target) or \
                   self.twoSumBSTs(root1.right, root2, target)
            
            
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
    print(f'Welcome to two sum bst')
    SOL = Solution()
    arr1 = [2,1,4]
    arr2 = [1,0,3]
    root1 = SOL.create_tree(arr1)
    root2 = SOL.create_tree(arr2)
    assert SOL.twoSumBSTs(root1, root2, target=5) == True

    arr1 = [0,-10,10]
    arr2 = [5,1,7,0,2]
    root1 = SOL.create_tree(arr1)
    root2 = SOL.create_tree(arr2)
    #TODO: Review this test case
    assert SOL.twoSumBSTs(root1, root2, target=18) == False

        