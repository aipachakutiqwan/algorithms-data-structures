'''

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

'''

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity: O(NM), where NxM is the size of the grid.
        Space Complexity: O(NM), where N is the size of the grid.
        '''
        queue = deque()
        # Insert in the queue the initial states of rotten oranges
        fresh_oranges = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j)) # append rotten orange position
                elif grid[i][j]== 1:
                    fresh_oranges +=1 
                    
        # Set the round with (-1,-1), every round will be separated by this marking
        queue.append((-1,-1))
        # Apply BFS and after every round set marker (-1,-1)
        minutes_elapsed = -1
        directions = [(-1,0),(+1,0),(0,-1),(0,+1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finished one round of processing
                minutes_elapsed+=1
                if queue: # to separate rounds and avoid endless loop
                    queue.append((-1,-1))
            else:
                # Process rotten orange from the queue contaminating its neighboards
                for d in directions:
                    neighboard_row, neighboard_col = row+d[0], col+d[1]
                    # verify that is not outside of the grid
                    if rows> neighboard_row >=0 and cols> neighboard_col>=0:
                        # neighboard position contains fresh orange
                        if grid[neighboard_row][neighboard_col] ==1:
                            # This orange would be marked as contaminated, added to queue
                            grid[neighboard_row][neighboard_col] = 2
                            fresh_oranges -=1
                            queue.append((neighboard_row, neighboard_col))
        
        return minutes_elapsed if fresh_oranges==0 else -1

if __name__ == "__main__":

    print(f'Welcome to rotting oranges problem')
    SOL = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    assert SOL.orangesRotting(grid) == 4

    grid = [[2,1,1],[0,1,1],[1,0,1]]
    assert SOL.orangesRotting(grid) == -1
                        

                    
                
                
        
        
        
        