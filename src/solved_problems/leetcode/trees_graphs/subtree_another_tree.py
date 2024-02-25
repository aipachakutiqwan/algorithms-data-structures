'''
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and 
node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree 
and ALL of this node's descendants. 
The tree tree could also be considered as a subtree of itself.

Example1:

       root:
          3    
        /   \      subroot:
       4     5         4
      / \             / \
    1    2           1   2

    output: True

Example 2:

       root:
          3
         / \        subroot:
        4   5          4
       / \            / \
      1   2          1   2
         /
        0 

    output: False (node descendants is not the same)

'''

# Definition for a binary tree node.
from typing import Optional
from queue import Queue

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Time Complexity: O(M*N), M and N number nodes of trees
        Space Complexity: O(M+N), There will be at most N recursive call to dfs (or isSubtree). 
            Now, each of these calls will have M recursive calls to isIdentical. Before calling isIdentical, 
            our call stack has at most O(N) elements and might increase to 
            O(N+M) during the call. After calling isIdentical, it will be back to at most 
            O(N) since all elements made by isIdentical are popped out. 
            Hence, the maximum number of elements in the call stack will be M+N.
        '''
        def is_identical(node1, node2):
            
            # if any node is empty, both should be empty to guarantee descendant similarity
            if node1==None or node2==None:
                return node1==None and node2==None
            else:
                # both are not empty, then to say identical, there are 3 conditions
                # 1. current values equal.
                # 2. left nodes are identical
                # 3. right nodes are identical
                return (node1.val==node2.val) and \
                        is_identical(node1.left, node2.left) and \
                        is_identical(node1.right, node2.right)
        
        def dfs(node):
            
            if node == None:
                # None tree node cannot be identical to a tree rooted at subRoot
                # which for problem constraint is not null
                return False
            else:
                # if tree rooted at node is identical to tree at subRoot
                if is_identical(node, subRoot):
                    return True
                # if tree rooted at node was not identical check children
                else:
                    return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
    

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
    print(f'Welcome to subtree of another tree problem')
    SOL = Solution()
    arr1 = [3,4,5,1,2]
    arr2 = [4,1,2]
    root = SOL.create_tree(arr1)
    sub_root = SOL.create_tree(arr2)
    assert SOL.isSubtree(root, sub_root) == True

    arr3 = [3,4,5,1,2,None,None,None,None,0]
    arr4 = [4,1,2]
    root = SOL.create_tree(arr3)
    sub_root = SOL.create_tree(arr4)
    assert SOL.isSubtree(root, sub_root) == False

            
            
        