
from collections import defaultdict
from queue import Queue


class BreathFirstSearh():

    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, v, w):
        self.graph[v].append(w)
    
    def bfs_iterative(self, s):
        print(f"Graph: {self.graph}")
        explored = {}
        explored[s] = 0
        q = Queue()
        q.put(s)
        while not q.empty():
            v = q.get()
            for w in self.graph[v]:
                if not explored.get(w) and (w not in explored):
                    explored[w] = explored[v] + 1 # for calculate shortest path when every note is weighted is only 1
                    print(f"explored: {w} distance: {explored[w]}")
                    q.put(w)
    
    def bfs_recursive(self, explored, q):
        if q.empty():
            return
        v = q.get()
        for w in self.graph[v]:
            if not explored.get(w) and (w not in explored):
                explored[w] = explored[v] + 1 # for calculate shortest path when every note is weighted is only 1
                print(f"explored: {w} distance: {explored[w]}")
                q.put(w)
        self.bfs_recursive(explored, q)


if __name__ == "__main__":
    print("welcome BFS")
    
    print("======= EXAMPLE 1 ======= ")
    BFS = BreathFirstSearh()
    """
    Example geeksforgeeks, start node 2
    """    
    BFS.add_edge(0,1)
    BFS.add_edge(0,2)
    BFS.add_edge(1,2)
    BFS.add_edge(2,0)
    BFS.add_edge(2,3)
    BFS.add_edge(3,3)
    print("BFS iterative:")
    BFS.bfs_iterative(2)
    print("BFS recursive:")
    # Initialize explored and queue with source vertex, in this case 2
    q = Queue()
    q.put(2)
    explored = {2:0} # O is set for the initial distance 0
    BFS.bfs_recursive(explored, q)

    print("======= EXAMPLE 2 ======= ")
    BFS = BreathFirstSearh()
    """
    Example coursera, start node "s"
    """
    BFS.add_edge('s','a')
    BFS.add_edge('s','b')
    BFS.add_edge('a','c')
    BFS.add_edge('b','c')
    BFS.add_edge('b','d')
    BFS.add_edge('c','e')
    BFS.add_edge('c','d')
    BFS.add_edge('d','e')
    print("BFS iterative:")
    BFS.bfs_iterative('s')
    print("BFS recursive:")
    # Initialize explored and queue with source vertex, in this case 2
    q = Queue()
    q.put('s')
    explored = {'s':0} # O is set for the initial distance 0
    BFS.bfs_recursive(explored, q)

