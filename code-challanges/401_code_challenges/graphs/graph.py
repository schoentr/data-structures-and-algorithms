from linked_list.linked_list import LinkedList
from stacks_and_queues.stacks_and_queues import Stack, Queue


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

    def get_neighbors(self, value):
        """This method return a list of all connections with a given node

        Arguments:
            node {vertix} 

        Returns:
            [list] -- A list of tuples (with the name, and weight)
        """
        output = []
        for item in self._graph[value]:
            output.append(item)
        return output

    def breadth_first(self, start):
        """This method does a breadth first traversal of a graph

        Arguments:
            node -- [starting poing of the traversal]

        Returns:
            [list] -- [a list of all connected nodes]
        """

        explored = []

        queue = Queue()
        queue.enqueue(start)

        while queue.peek() is not None:
            node = queue.dequeue()
            if node not in explored:
                explored.append(node)

                neighbors = self._graph[node]
                for neighbor in neighbors:
                    queue.enqueue(neighbor[0])
        return explored

    def depth_first(self, start):
        visited = []
        s = Stack()
        s.push(start)
        visited.append(start)
        while s.is_empty() == False:
            curr = s.peek()
            flag = False
            for neighbor in self.get_neighbors(curr):
                if neighbor[0] not in visited and flag == False:
                    s.push(neighbor[0])
                    visited.append(neighbor[0])
                    flag = True
            if flag == False:
                s.pop()
        return visited


class Vertex:
    """This makes a vertex
    """

    def __init__(self, value):
        self.value = value

    # def __repr__(self):
