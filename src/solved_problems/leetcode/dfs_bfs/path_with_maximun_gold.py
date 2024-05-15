'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
'''
from typing import List


class Solution:

    def dfs_backtrack(self, grid, rows, cols, row, col, directions):    
        if row < 0 or col < 0 or row>=rows or col>=cols or grid[row][col]==0:
            return 0
        max_gold = 0
        original_val = grid[row][col]
        grid[row][col] = 0
        for i in range(len(directions)-1):
            max_gold = max(max_gold, self.dfs_backtrack(grid, rows, cols, 
                           row + directions[i], 
                           col + directions[i + 1], 
                           directions))
        grid[row][col] = original_val
        return max_gold + original_val


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        '''
        Solved using Deep First Search with backtracking approach.
        Let n be the number of rows in the grid, m be the number of columns, and g be the number of gold cells.

        Time complexity: O(m*n*4ˆg) 
        In the getMaximumGold function, we call the dfsBacktrack function once for each cell in the grid, totaling m*n times.
        The backtrack function recursively calls itself. Each time we call the dfsBacktrack function from a cell containing gold, 
        4 recursive calls are made. That means the backtrack function can be called up to 4^g times for a given starting cell.
        Therefore, the overall time complexity is O(m⋅n⋅4ˆg)

        Space complexity: O(g)
        Since the length of a path through gold cells can be g, the recursive call stack can grow up to size g.

        '''
        directions = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0
        for row in range(rows):
            for col in range(cols):
                max_gold = max(max_gold, self.dfs_backtrack(grid, rows, cols, row, col, directions))
        return max_gold

if __name__ == "__main__":
    print(f'Welcome to Path with Maximun Gold solution problem')
    SOL = Solution()
    grid = [[0,6,0],[5,8,7],[0,9,0]]
    assert SOL.getMaximumGold(grid) == 24
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    SOL.getMaximumGold(grid)
    assert SOL.getMaximumGold(grid) == 28




        