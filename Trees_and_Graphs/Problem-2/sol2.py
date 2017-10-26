from Trees_and_Graphs.graph.main import Graph
from Trees_and_Graphs.vertex.main import Vertex
from Stacks_and_Queues.queue.main import Queue

import sys


class BFSGraph(Graph):
    """
    A derived class from Graph base class
    """

    #
    # Run time for dfs => O(V+E)
    #
    def __init__(self):
        super().__init__()

    def bfs_visit(self, start_vertex, end_vertex):
        """
        Args:
            start_vertex(Vertex): The starting node for BFS
            end_vertex(Vertex): The end point in the path
        Returns:
            Boolean: Indicates if a path exists between
                start and end vertices
        """
        if start_vertex == end_vertex:
            return True
        start_vertex.setDistance(0)
        start_vertex.setPredecessor(None)
        vert_queue = Queue()
        vert_queue.enqueue(start_vertex)
        while vert_queue.size() > 0:
            current_vert = vert_queue.dequeue()
            for v in current_vert.getConnections():
                print(v.id)
                if v.getColor() == 'white':
                    v.setPredecessor(start_vertex)
                    if v == end_vertex:
                        print(v.id)
                        return True
                    else:
                        v.setColor('gray')
                        vert_queue.enqueue(v)
            current_vert.setColor('black')
        return False


g = BFSGraph()

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

print(g.bfs_visit(g.get_vertex(a.id), g.get_vertex(e.id)))