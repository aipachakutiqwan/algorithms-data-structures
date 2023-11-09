
"""
It is working but need more test cases
"""

class ShortestPaths:

    def __init__(self) -> None:
        pass

    def read_file(self, file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
        dict_graph = {}
        for line in lines:
            split_line = line.split()
            vertex = split_line[0]
            elements = split_line[1:]
            children = []
            for elem in elements:
                value = elem.split(",")
                dict_elem = {}
                dict_elem[value[0]] = int(value[1])
                children.append(dict_elem)
            dict_graph[vertex] = children
        return dict_graph
    

    def calculate_shortest_path(self, dict_graph):

        X = {}
        graph_keys = list(dict_graph.keys())
        X[graph_keys[0]]=0
        
        A  = []
        A.append(0)

        while len(X) <= len(dict_graph):

            last_processed_vertex = list(X.keys())[-1]
            first = True
            min_distance = None
            min_node = None

            for next_candidate_node in dict_graph[last_processed_vertex]:
                for processed_node in X.items():
                    processed_node_value = processed_node[0]
                    processed_node_distance = processed_node[1]
                    next_candidate_value = list(next_candidate_node.keys())[0]
                    children_processed_node = dict_graph[processed_node_value]
                    children_processed_node_keys = list(map(lambda x: [*x][0], children_processed_node))
                    children_processed_node_values = list(map(lambda x: [*x.values()][0], children_processed_node))

                    if next_candidate_value in children_processed_node_keys:
                        pos = children_processed_node_keys.index(next_candidate_value)
                        next_candidate_distance = children_processed_node_values[pos]
                        path_distance = processed_node_distance + next_candidate_distance
                            
                        if first:
                                min_distance = path_distance
                                min_node = next_candidate_value
                                first = False
                        elif path_distance <  min_distance:
                            min_distance = path_distance
                            min_node = next_candidate_value
            
            X[min_node] = min_distance
            A.append(min_distance)
        return X, A


if __name__ == "__main__":
    print("Welcome to ShortestPath")
    PATH_FILE = "files/directed-dijkstra.txt"
    SP = ShortestPaths()
    dict_graph = SP.read_file(PATH_FILE)
    X, A = SP.calculate_shortest_path(dict_graph)
    print(X)
    print(A)
