
'''
Given the root of a binary tree, return the sum of values of its deepest leaves.

                        1
                     /     \
                    2       3
                  /   \       \
                 4     5       6
                /                \
               7                  8
answer: 7 + 8 = 15
               
'''
# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Use both ways to create queues in Python
from collections import deque
from queue import Queue

from typing import Optional

class Solution:
    
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        '''
        Solved with DFS approach.
        Time complexity: 0(n)
        Space complexity: 0(n)
        
        '''
        
        q = deque()
        q.append(root)
        q.append(None)
        final_sum = 0
        partial_sum = 0
        # Queue will have always 2 elements as minimun
        
        while q:
            
            node = q.popleft()
            
            while node!=None:
                
                partial_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                node = q.popleft()
                
            # After a level traversal add a final level marker as None element
            q.append(None)
            # Store level sum
            final_sum = partial_sum
            partial_sum = 0
            # If there is only one element (None), that means we arrived to the end of the three
            if len(q)==1:
                break
        
        return final_sum

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
                    if node:
                        q.put(node.left)
                        count+=1
                else:
                    break

                if count < len(arr):
                    if arr[count] != None:
                        node.right = TreeNode(arr[count])
                    if node:
                        q.put(node.right)
                        count+=1
                else:
                    break
        return root

if __name__ == "__main__":
    print(f'Deepest Leaves Sum')
    SOL = Solution()
    arr = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = SOL.create_tree(arr)
    assert SOL.deepestLeavesSum(root) == 15
    arr = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
    root = SOL.create_tree(arr)
    assert SOL.deepestLeavesSum(root) == 19
            
            
            

            
                    
                    
            
                
                
                
                    
        
        

