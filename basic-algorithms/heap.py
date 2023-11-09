from __future__ import annotations
from typing import List, Optional

import sys


class MinHeap:
    """
    Abstracting the node data as Int but could be Any, given a custom comparison
    function to guide ourselves on how to compare the nodes.
    """

    def __init__(self, nodes: List[int] = []):
        self.nodes = []
        for node in nodes:
            self.insert_node(node)

    def __len__(self) -> int:
        return len(self.nodes)

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, parent_index: int) -> bool:
        return self.__get_left_child_index(parent_index) < len(self.nodes)

    def __has_right_child(self, parent_index: int) -> bool:
        return self.__get_right_child_index(parent_index) < len(self.nodes)

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index: int) -> Optional[int]:
        if not self.__has_left_child(index):
            # Virtual -inf
            return -sys.maxsize
        return self.nodes[self.__get_left_child_index(index)]

    def __right_child(self, index: int) -> Optional[int]:
        if not self.__has_right_child(index):
            # Virtual -inf
            return -sys.maxsize
        return self.nodes[self.__get_right_child_index(index)]

    def __parent(self, index: int) -> Optional[int]:
        if not self.__has_parent(index):
            return None
        return self.nodes[self.__get_parent_index(index)]
    
    # INSERT AND BUBBLE-UP
    def __swap(self, first_idx: int, second_idx: int):
        if first_idx >= len(self.nodes) or second_idx >= len(self.nodes):
            print(f'first ({first_idx}) or second ({second_idx}) are invalid')
            return
        self.nodes[first_idx], self.nodes[second_idx] = self.nodes[second_idx], self.nodes[first_idx]


    def __bubble_up(self, child_index: Optional[int] = None):
        """Move last added element to correct position in heap"""
        if not child_index:
            # Start with last
            child_index = len(self.nodes) - 1
        # Check if smaller than parent
        parent_idx = self.__get_parent_index(child_index)
        if self.__parent(child_index) and self.nodes[child_index] < self.__parent(child_index):
            # Swap child <> parent
            self.__swap(child_index, parent_idx)
            # Recurse on parent index now (should have child value)
            self.__bubble_up(child_index=parent_idx)
        # If its not smaller, leave as it is
        return self.nodes

    def insert_node(self, item: int):
        self.nodes.append(item)
        self.__bubble_up()
        return self.nodes

    # EXTRACT_MIN AND BUBBLE-DOWN
    def __bubble_down(self, index: Optional[int] = 0):
        """Move root to proper position in heap"""
        if index >= len(self.nodes) or not self.__has_left_child(index): # perfectly balanced since need to have left to exist next nodes
            return self.nodes
        # Check if greater than left or right
        smaller_child_idx = self.__get_left_child_index(index)

        if self.__has_right_child(index) and \
        self.__right_child(index) < self.__left_child(index):
            smaller_child_idx = self.__get_right_child_index(index)

        if self.nodes[index] < self.nodes[smaller_child_idx]:
            # Lower than both, do nothing
            return self.nodes

        if self.nodes[index] > self.nodes[smaller_child_idx]:
            # Swap with smaller child
            self.__swap(index, smaller_child_idx)
            return self.__bubble_down(smaller_child_idx)

    def extract_minimun(self) -> Optional[int]:
        """
        Extract minimun lowest element from the heap (usually root). To avoid memory shift
        of first-element removal, we copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
        if self.is_empty():
            print('Empty, not extracting')
            return None

        # Remove first and insert the last one added as the root
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[len(self.nodes) - 1]
        # Shrink size by 1
        # Could've also used self.nodes = self.nodes[:-1]
        del self.nodes[-1]
        self.__bubble_down()
        return removed_node
    
    # PRINT MINIMUN
    def is_empty(self) -> bool:
        return not self.nodes

    def print_minimun(self) -> Optional[int]:
        if self.is_empty():
            print('Empty, not extracting')
            return None
        return self.nodes[0]
    
    # EXTRACT SPECIFIC ELEMENT
    def delete_element(self, element):

        index_remove = None
        print(f'self.nodes: {self.nodes}')
        for pos in range(len(self.nodes)):
            if element == self.nodes[pos]:
                index_remove = pos
                break
        print(f'index_remove: {index_remove}')
        removed_node = self.nodes[index_remove]
        self.nodes[index_remove] = self.nodes[len(self.nodes) - 1]
        del self.nodes[-1]
        self.__bubble_down(index_remove)
        return self.nodes



if __name__ == "__main__":
    #list = [1,23]
    MH = MinHeap([])
    nodes_status = MH.insert_node(10)
    nodes_status = MH.insert_node(30)
    nodes_status = MH.insert_node(20)
    nodes_status = MH.insert_node(400)
    print(nodes_status)
    nodes_status = MH.delete_element(30)
    print(nodes_status)
    #nodes_status = MH.extract_minimun()
    #print(nodes_status)
    #nodes_status = MH.extract_minimun()
    #print(nodes_status)
    #nodes_status = MH.extract_minimun()
    #print(nodes_status)
    #nodes_status = MH.print_minimun()
    #print(nodes_status)
    





