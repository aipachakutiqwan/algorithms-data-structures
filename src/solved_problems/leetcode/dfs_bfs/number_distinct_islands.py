'''
You are given an m x n binary matrix grid. 
An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
An island is considered to be the same as another if and 
only if one island can be translated (and not rotated or reflected) to equal the other.
Return the number of distinct islands.

'''

from typing import List

class Solution:

    def dfs(self, row, col, initial_row, initial_col, seen, island, grid):
        if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]):
            return
        if grid[row][col] == 0 or (row, col) in seen:
            return
        seen.add((row, col))
        # move the first element of the list to the coordinate (0,0),
        # in this way it is obtained comparable island coordinates.
        island.add((row-initial_row, col-initial_col))
        self.dfs(row+1, col, initial_row, initial_col, seen, island, grid)
        self.dfs(row-1, col, initial_row, initial_col, seen, island, grid)
        self.dfs(row, col+1, initial_row, initial_col, seen, island, grid)
        self.dfs(row, col-1, initial_row, initial_col, seen, island, grid)


    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        '''
        Solved using DFS approach. 
        
        Let M be the number of rows, and N be the number of columns.

        Time complexity: We're inserting each cell into a hash table (corresponding to the island it is a part of), 
        and then inserting each of those hash tables into another hash table.
        The cost of inserting each of the M⋅N cells into its initial hash table is O(1), 
        so those insertions have a total complexity of O(M⋅N).
        To insert the "island" hash tables into the final hash table, 
        each of them has to (within the library code) be hashed by a hash function. 
        While often we assume that the process of hashing is O(1), 
        in this we can't as the inputs to be hashed could be arbitrarily large. 
        So instead, the cost of hashing them is linearly proportional to the number of cells in the hash table being hashed. 
        Each cell is essentially getting hashed once in this process too though (as each can only be a part of one island), 
        and so this part is also O(M⋅N).
        As both phases have a time complexity of O(M⋅N), this is the total time complexity.
        Be aware that the time complexity of this approach is dependent on a good hash function. 
        
        Space complexity: M*N, The seen set is the biggest use of additional memory.
        
        '''
        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                island = set()
                initial_row = row
                initial_col = col
                self.dfs(row, col, initial_row, initial_col, seen, island, grid)
                if island:
                    # frozenset hash all the entire set island.
                    # and accept adding if there was not present previously
                    unique_islands.add(frozenset(island))
        return len(unique_islands)
                
if __name__ == "__main__":
    print('Welcome to Number of distinct islands')
    SOL = Solution()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    assert SOL.numDistinctIslands(grid) == 1

    grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
    assert SOL.numDistinctIslands(grid) == 3




        