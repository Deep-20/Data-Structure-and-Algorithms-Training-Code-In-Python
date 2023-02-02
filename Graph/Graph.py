class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                pass

        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            while len(self.adjacency_list[vertex]) != 0:
                self.remove_edge(vertex, self.adjacency_list[vertex][0])

            self.adjacency_list.pop(vertex)
            return True
        return False

    
    # BFS Traversal
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]

        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.adjacency_list[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    # DFS Traversal
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]

        while stack:
            topVertex = stack.pop()                 # Or stack.pop(-1)
            print(topVertex)
            for adjacentVertex in self.adjacency_list[topVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customGraph = Graph()

customGraph.add_vertex("A")
customGraph.add_vertex("B")
customGraph.add_vertex("C")
customGraph.add_vertex("D")

customGraph.add_edge("A", "B")
customGraph.add_edge("C", "B")
customGraph.add_edge("A", "C")
customGraph.add_edge("A", "D")
customGraph.add_edge("D", "C")

# customGraph.print_graph()

# customGraph.remove_edge("A", "D")

# customGraph.remove_vertex("A")

# print("--------------------")
# customGraph.print_graph()

# customGraph.bfs("A")
customGraph.dfs("A")
