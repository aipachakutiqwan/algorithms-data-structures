'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only 
one way to travel between two different cities (this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction 
because they are too narrow.
Roads are represented by connections where connections[i] = [ai, bi] 
represents a road from city ai to city bi.
This year, there will be a big event in the capital (city 0), 
and many people want to travel to this city.
Your task consists of reorienting some roads such that each 
city can visit the city 0. Return the minimum number of edges changed.
It's guaranteed that each city can reach city 0 after reorder.
'''
from typing import List
from queue import Queue

class Solution:

    def __init__(self):
        self.count = 0

    def dfs(self, node: int, parent: int, adj_dict: dict):
        '''
        DFS approach 
        Time complexity: 0(n)
        Space complexity: 0(n)
        '''
        if not node in adj_dict:
            return
        for neighbor in adj_dict[node]:
            neighbor_value = neighbor[0]
            neighbor_direction = neighbor[1]
            if neighbor_value != parent:
                self.count += neighbor_direction
                self.dfs(neighbor_value, node, adj_dict)
    
    def bfs(self, adj_dict:dict, q, dict_explored):
        '''
        BFS approach 
        Time complexity: 0(n)
        Space complexity: 0(n)
        '''
        if q.empty():
            return
        v = q.get()
        for w in adj_dict[v]:
            if w[0] not in dict_explored:
                self.count += w[1]
                dict_explored[w[0]] = 1
                q.put(w[0])
        self.bfs(adj_dict, q, dict_explored)
                

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        adj_dict = {}
        for a, b in connections:
            if a in adj_dict:
                adj_dict[a].append((b, 1))
            else:
                adj_dict[a]=[(b, 1)]
            if b in adj_dict:
                adj_dict[b].append((a, 0))
            else:
                adj_dict[b]=[(a, 0)]
        # DFS approach
        self.dfs(0, -1, adj_dict) # start with parent -1 (artificial parent)
        # BFS approach
        #q = Queue()
        #q.put(0)
        #dict_explored = {0:1} # 1 is just to indicate existence element in dict
        #self.bfs(adj_dict, q, dict_explored)          
        return self.count

if __name__ == "__main__":
    print(f'Welcome to Reorder Routes to Make all Paths Lead to the City Zero')
    SOL = Solution()    
    n = 6
    connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    assert SOL.minReorder(n, connections) == 3
    SOL = Solution() 
    n = 5
    connections = [[1,0],[1,2],[3,2],[3,4]]
    assert SOL.minReorder(n, connections) == 2
    SOL = Solution() 
    n = 3
    connections = [[1,0],[2,0]]
    assert SOL.minReorder(n, connections) == 0

    





                
                
                
                
                
                
                
                
                
            
            
