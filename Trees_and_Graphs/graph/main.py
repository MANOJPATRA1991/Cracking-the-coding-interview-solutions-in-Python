from Trees_and_Graphs.vertex.main import Vertex


class Graph:
    """
    Attributes:
        vert_list(dict): A dictionary of the vertices in the graph
        num_vertices(int): Number of vertices in the graoh
    """

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        """
        Add a vertex to the graph
        Args:
            key(int/string): The key of the Vertex object
        Returns:
            Vertex: The newly added vertex
        """
        self.num_vertices = self.num_vertices + 1     # increment numVertices
        new_vertex = Vertex(key)     # create a Vertex object with passed key
        self.vert_list[key] = new_vertex      # add the new vertex to the vertList as value of the passed key of this Graph
        return new_vertex        # return the new vertex

    def get_vertex(self, n):
        """
        Get vertex from this Graph
        Args:
            n: The key to search for in the Graph
        Returns:
            Vertex: If key 'n' is in vertList, return vertList[n]; else return None
        """
        if n in self.vert_list:      # if key 'n' is in vertList
            return self.vert_list[n]     # return vertList[n]
        else:
            return None     # else return None

    def __contains__(self, item):
        """
        Returns True if item is in vertList
        Args:
            item(int): Key to search for in the vertList
        """
        return item in self.vert_list

    def add_edge(self, f, t, cost=0):
        """
        Add edge between two vertices in the graph if they exist
        Args:
            f(int/string): First key in vertList
            t(int/string): Second key in vertList
            cost(int, optional): Weight of the edge
                            that connects the two vertices
        """
        if f not in self.vert_list:
            new_vertex = self.add_vertex(f)
        if t not in self.vert_list:
            new_vertex = self.add_vertex(t)
        self.vert_list[f].addNeighbor(self.vert_list[t], cost)

    def get_vertices(self):
        """
        Returns the names of all the vertices in the graph
        """
        return self.vert_list.keys()

    def __iter__(self):
        """
        Return an Iterator object to iterate over all the
        Vertex objects in a particular graph
        """
        return iter(self.vert_list.values())

    def transpose_graph(self):
        """
        Transpose the Graph by reversing the edges
        Required for strongly connected components algorithm
        """
        tmp = []
        for v in self:
            for key in list(v.getConnections()):
                if (v,key) not in tmp or (key, v) not in tmp:
                    key.connectedTo[v] = v.connectedTo[key]
                    tmp.append((v, key))
                    tmp.append((key, v))
                    del v.connectedTo[key]
