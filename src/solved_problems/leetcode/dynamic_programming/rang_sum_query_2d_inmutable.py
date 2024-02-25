'''
Given a 2D matrix matrix, handle multiple queries of the following type:
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).

Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) 
Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) 
and lower right corner (row2, col2).

You must design an algorithm where sumRegion works on O(1) time complexity.
'''
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dp = []
        for row in range(len(matrix)):
            cumulative_col = 0
            temp_row = []
            for col in range(len(matrix[0])):
                cumulative_col += matrix[row][col]
                if row == 0:
                    temp_row.append(cumulative_col)
                else:
                    temp_row.append(cumulative_col + self.dp[row-1][col])
            self.dp.append(temp_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        Time Complexity:  0(1)
        Space Complexity: 0(rows*cols)
        '''
        # If there is the same position, it is enought to return the matrix position value
        if row1==row2==col1==col2:
            return self.matrix[row1][col1]
        # The following is for avoid calculate wrong positions (eg. [-1][-1])
        if row1-1 >=0:
            a = self.dp[row1-1][col2]
        else:
            a = 0
        
        if col1-1 >=0:
            b = self.dp[row2][col1-1]
        else:
            b = 0

        if row1-1 >=0 and col1-1>=0:
            c = self.dp[row1-1][col1-1]
        else:
            c = 0

        sum_region = self.dp[row2][col2] - a - b + c
        return sum_region
        

if __name__ == "__main__":
    
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    SOL = NumMatrix(matrix)
    assert SOL.sumRegion(2, 1, 4, 3) == 8
    assert SOL.sumRegion(1, 1, 2, 2) == 11
    assert SOL.sumRegion(1, 2, 2, 4) == 12



    
