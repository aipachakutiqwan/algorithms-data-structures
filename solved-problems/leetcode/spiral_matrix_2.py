'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
1 -> 2 -> 3
8 -> 9    4
7 <- 6 <- 5

'''
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        Time complexity: O(nˆ2)
        Space complexity: O(nˆ2)
        '''
        m= []
        for i in range(n):
            col = []
            for j in range(n):
                col.append(-1)
            m.append(col)
        
        counter = 0
        layers = (n+1)//2
        
        for layer in range(layers):
            
            # left -> right
            for i in range(layer, n-layer):
                counter +=1
                m[layer][i] = counter
            
            # top -> bottom
            for j in range(layer+1, n-layer):
                counter+=1
                m[j][n-layer-1] = counter
            
            # right -> left
            for i in range(n-layer-2, layer-1, -1):
                counter+=1
                m[n-layer-1][i] = counter
            
            # bottom -> top
            for j in range(n-layer-2, layer,  -1):
                counter+=1
                m[j][layer] = counter
        
        return m
        
if __name__ == "__main__":
    print('Welcome to spiral matrix problem.')
    n = 3
    SOL = Solution()
    assert SOL.generateMatrix(n) ==  [[1,2,3],[8,9,4],[7,6,5]]
    n = 1
    assert SOL.generateMatrix(1) ==  [[1]]


