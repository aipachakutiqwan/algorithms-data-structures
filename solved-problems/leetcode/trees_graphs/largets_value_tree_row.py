'''
Given the root of a binary tree, 
return an array of the largest value in each row of the tree (0-indexed).
          1
        /   \    
       3     2
     /  \     \
    5   3      9
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

'''
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

from collections import deque
from typing import Optional, List

class Solution:
    
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Deep Breath First solution.
        '''

        answer = []
        if not root:
            return answer
            
        q = deque()
        q.append(root)
        
        while q:

            size_queue = len(q)
            max_value = float('-inf')
            for i in range(size_queue):
                node = q.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            answer.append(max_value)
        
        return answer

    
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
    print(f'Find Largest Value in Each Tree Row')
    SOL = Solution()
    arr = [1,3,2,5,3,None,9]
    root = SOL.create_tree(arr)
    assert SOL.largestValues(root) == [1,3,9]
    arr = [1,2,3]
    root = SOL.create_tree(arr)
    assert SOL.largestValues(root) == [1,3]


        
        
        