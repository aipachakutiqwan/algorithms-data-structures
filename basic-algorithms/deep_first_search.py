
from collections import defaultdict
from collections import deque

class DeepFirstSearch:

    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, v, w):
        self.graph[v].append(w)
    
    def dfs_recursive(self, v, explored):
        print(f"explored: {v}")
        explored[v] = True
        for w in self.graph[v]:
            if not explored.get(w):
                self.dfs_recursive(w, explored)

    def dfs_iterative(self, v):
        explored = {}
        stack = deque()
        stack.append(v)
        
        while stack:
            v = stack.pop()
            if not explored.get(v):
                print(f"explored: {v}")
                explored[v] = True

            for w in self.graph[v]:
                if not explored.get(w):
                    stack.append(w)



if __name__ == "__main__":
    print(f"Welcome DFS")
    DFS = DeepFirstSearch()
    DFS.add_edge('s','a')
    DFS.add_edge('a','s')
    DFS.add_edge('a','c')
    DFS.add_edge('c','a')
    DFS.add_edge('b','a')
    DFS.add_edge('a','b')
    DFS.add_edge('b','s')
    DFS.add_edge('s','b')
    DFS.add_edge('c','e')
    DFS.add_edge('e','c')
    DFS.add_edge('d','c')
    DFS.add_edge('c','d')
    DFS.add_edge('d','b')
    DFS.add_edge('b','d')
    DFS.add_edge('e','d')
    DFS.add_edge('d','e')
    print("Recursive:")
    DFS.dfs_recursive('s', {})
    print("Iterative:")
    DFS.dfs_iterative('s')
