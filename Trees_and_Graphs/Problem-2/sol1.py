from Trees_and_Graphs.graph.main import Graph
from Trees_and_Graphs.vertex.main import Vertex
import sys


class DFSGraph(Graph):
    """
    A derived class from Graph base class
    """

    #
    # Run time for dfs => O(V+E)
    #
    def __init__(self):
        super().__init__()

    def dfs_visit(self, start_vertex, end_vertex):
        """
        Args:
            start_vertex(Vertex): The starting node for DFS
            end_vertex(Vertex): The end point in the path
        """
        # Run-time => O(E) for the for loop
        #
        # as the loop will execute a max of once for every edge
        #
        # Recursive call occurs only if color of vertex is white
        if start_vertex == end_vertex:
            return True
        start_vertex.setColor('gray')
        for v in start_vertex.getConnections():
            if v.getColor() == 'white':
                v.setPredecessor(start_vertex)
                if v == end_vertex:
                    return True
                else:
                    v.setColor('gray')
                    self.dfs_visit(v, end_vertex)
        return False


g = DFSGraph()

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')

g.add_vertex(a.id)
g.get_vertex(a.id).setDistance(sys.maxsize)
g.add_vertex(b.id)
g.get_vertex(b.id).setDistance(sys.maxsize)
g.add_vertex(c.id)
g.get_vertex(c.id).setDistance(sys.maxsize)
g.add_vertex(d.id)
g.get_vertex(d.id).setDistance(sys.maxsize)
g.add_vertex(e.id)
g.get_vertex(e.id).setDistance(sys.maxsize)
g.add_vertex(f.id)
g.get_vertex(f.id).setDistance(sys.maxsize)

g.add_edge(a.id, b.id, 2)
g.add_edge(a.id, c.id, 5)
g.add_edge(a.id, d.id, 1)
g.add_edge(b.id, a.id, 2)
g.add_edge(b.id, c.id, 3)
g.add_edge(b.id, d.id, 2)
g.add_edge(c.id, a.id, 5)
g.add_edge(c.id, b.id, 3)
g.add_edge(c.id, d.id, 3)
g.add_edge(c.id, e.id, 1)
g.add_edge(c.id, f.id, 5)
g.add_edge(d.id, a.id, 1)
g.add_edge(d.id, b.id, 2)
g.add_edge(d.id, c.id, 3)
g.add_edge(d.id, e.id, 1)
g.add_edge(e.id, d.id, 1)
g.add_edge(e.id, c.id, 1)
g.add_edge(e.id, f.id, 1)
g.add_edge(f.id, c.id, 5)
g.add_edge(f.id, e.id, 1)

print(g.dfs_visit(g.get_vertex(a.id), g.get_vertex(c.id)))