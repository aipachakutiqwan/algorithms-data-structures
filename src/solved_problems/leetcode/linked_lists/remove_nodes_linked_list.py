from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNodes_stack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Solved using stack approach.

        Time complexity: O(n)
            Adding the nodes from the original linked list to the stack takes O(n).
            Removing nodes from the stack and adding them to the result takes O(n), 
            as each node is popped from the stack exactly once.
            Therefore, the time complexity is O(2n), which simplifies to O(n).
        Space complexity: O(n)
            We add each of the nodes from the original linked list to the stack, making its size n.
            We only use resultList to store the result, so it does not contribute to the space complexity.
            Therefore, the space complexity is O(n).
        '''
        current = head
        stack = deque()

        while current:
            stack.append(current)
            current = current.next

        current = stack.pop()
        maximun = current.val
        result_list = ListNode(maximun)

        while stack:
            current = stack.pop()
            if current.val < maximun:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximun = current.val
        
        return result_list

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Let n be the length of the original linked list.

        Time complexity: O(n)
        We call removeNodes() once for each node in the original linked list. 
        The other operations inside the function all take constant time, 
        so the time complexity is dominated by the recursive calls. 
        Thus, the time complexity is O(n).
        Space complexity: O(n)
        Since we make n recursive calls to removeNodes(), 
        the call stack can grow up to size n. Therefore, the space complexity is O(n).
        '''

        if head==None or head.next==None:
            return head
        next_node = self.removeNodes(head.next)
        if head.val < next_node.val:
            head.val = next_node.val
            head.next = next_node.next
            return head
        else:
            return head
    
    def create_linked_list(self, list_values):
        first = True
        head = None
        traverse = None
        for value in list_values:
            if first:
                head = ListNode(value)
                traverse = head
                first = False
            else:
                new_node = ListNode(value)
                traverse.next = new_node
                traverse =  traverse.next
        return head

        
        
if __name__ == "__main__":

    print('Welcome to Remove Nodes from Linked List')
    SOL = Solution()
    list_values = [5,2,13,3,8]
    head = SOL.create_linked_list(list_values)
    output_list = SOL.removeNodes(head)
    for value in [13,8]:
        assert output_list.val == value
        output_list = output_list.next

    list_values = [1,1,1,1]
    head = SOL.create_linked_list(list_values)
    output_list = SOL.removeNodes(head)
    for value in [1,1,1,1]:
        assert output_list.val == value
        output_list = output_list.next






        

        