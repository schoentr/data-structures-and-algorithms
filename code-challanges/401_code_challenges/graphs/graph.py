from linked_list.linked_list import LinkedList


class Graph:

    def __init__(self):
        """Initializes the graph class as an empty dictionary
        """

        self._graph = {}

    def add(self, value):
        """This method takes in a value and adds it to the graph

        Arguments:
            value {} 

        Returns:
            [Node/Vertex] --  return a node with the value
        """
        vertex = Vertex(value)
        self._graph[value] = []
        return vertex

    def add_edge(self, node_a, node_b, weight=1):
        """This adds an edge between two verticies
        
        Arguments:
            node_a {node/vertex} 
            node_b {node/vertex} 
        
        Keyword Arguments:
            weight {int} -- the weight of the edge (default: {1})
        """

        self._graph[node_a.value].append((node_b.value, weight))
        self._graph[node_b.value].append((node_a.value, weight))

    def get_vertices(self):
        """This return a list of all vertices in the graph
        
        Returns:
            [list] -- [a list of all the vertices]
        """
        output = []
        for key in self._graph.keys():
            output.append(key)
        return output

    def size(self):
        """This method returns the number of nodes in the graph
        
        Returns:
            [int] 
        """

        output = []
        for key in self._graph.keys():
            output.append(key)
        return len(output)

    def get_neighbors(self, node):
        """This method return a list of all connections with a given node
        
        Arguments:
            node {vertix} 
        
        Returns:
            [list] -- A list of tuples (with the name, and weight)
        """
        output = []
        for item in self._graph[node.value]:
            output.append(item)
        return output


class Vertex:
    """This makes a vertex
    """

    def __init__(self, value):
        self.value = value

    # def __repr__(self):
