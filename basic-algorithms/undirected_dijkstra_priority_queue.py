"""
CORRECT:
2599,2610,2947,2052,2367,2399,2029,2442,2505,3068


"""

from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    
    def __str__(self) -> str:
        return str(self.edges)

    def add_edge(self, u, v, weight):
            self.edges[u][v] = weight
            self.edges[v][u] = weight
    
    def read_graph(self, path_file):
        with open(path_file, "r") as file:
            file_lines = file.readlines()
        
        for line in file_lines:
            arr_line = line.split()
            u = int(arr_line[0])
            for node in range(1, len(arr_line)):
                node = arr_line[node].split(',')
                v = int(node[0])
                weight = int(node[1])
                self.add_edge(u, v, weight) 


def dijkstra(graph, start_vertex):
    
    D = { v: float('inf') for v in range(graph.v)} # D store distances to the nodes/vertices
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():

        (dist, current_vertex) = pq.get() # obtain the node with the minimun distance
        graph.visited.append(current_vertex)

        for neighbor in range(graph.v): # verify for all the nodes

            if graph.edges[current_vertex][neighbor] != -1: # verify there is connectivity between node and neighbor
                distance = graph.edges[current_vertex][neighbor] # distance between current and neighbor

                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance

                    if new_cost < old_cost: # since started as infinite and it is needed the minimun distance
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D


if __name__ == "__main__":
    path_file = "files/indirected-dijkstra.txt"
    g_class = Graph(201)
    g_class.read_graph(path_file)
    #print(str(g_class))
    D = dijkstra(g_class, 1)

    results_keys = [7,37,59,82,99,115,133,165,188,197]
    for key in results_keys:
        print(f"key {key}: {D[key]}")

    #for vertex in range(len(D)):
    #    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
    #print(D)



