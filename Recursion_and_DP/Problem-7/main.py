from Trees_and_Graphs.graph.main import Graph


class DFSGraph(Graph):
    """
    A derived class from Graph base class
    """
    def __init__(self):
        super().__init__()
        self.rows = 0
        self.cols = 0

    def dfs(self, x, y, new_color):
        """
        Starts the depth first search
        Args:
            x: Row number
            y: Column number
            new_color: New color to set for this position
        """
        start_vertex = paint_graph.get_vertex((x, y))
        old_color = start_vertex.getColor()
        start_vertex.setColor(new_color)
        self.dfs_visit(old_color, new_color, start_vertex)

    def dfs_visit(self, old_color, new_color, start_vertex):
        """
        Perform DFS
        Args:
            start_vertex: Vertex at which to do DFS
            old_color: Old color at given vertex
            new_color: New color to set
        """
        for v in start_vertex.getConnections():
            if v.getColor() == old_color:
                v.setColor(new_color)
                self.dfs_visit(old_color, new_color, v)

    def make_grid_color(self, color_list):
        """
        Make new grid
        Args:
            color_list: List used to make the grid
        """
        self.rows = len(color_list)
        self.cols = len(color_list[0])
        # Create the grid
        for i in range(self.rows):
            for j in range(self.cols):
                new_vertex = self.add_vertex((i, j))
                new_vertex.setColor(color_list[i][j])

        # Add connections for each vertex in the graph
        for vert in self:
            connected_to = {}
            if vert.id[0] - 1 >= 0:
                connected_to[self.get_vertex((vert.id[0] - 1, vert.id[1]))] = 0
            if vert.id[0] + 1 < self.rows:
                connected_to[self.get_vertex((vert.id[0] + 1, vert.id[1]))] = 0
            if vert.id[1] + 1 < self.cols:
                connected_to[self.get_vertex((vert.id[0], vert.id[1] + 1))] = 0
            if vert.id[1] - 1 >= 0:
                connected_to[self.get_vertex((vert.id[0], vert.id[1] - 1))] = 0
            vert.connectedTo = connected_to

    def print_paint_graph(self):
        """
        Prints the paint graph
        """
        count = 0
        for vertex in self:
            if count != 0 and count % self.cols == 0:
                print("\n")
            count += 1
            print(vertex.getColor(), ' ', end='')
        print("\n")
        print("--------------------------------")

# Create a new graph
paint_graph = DFSGraph()
# Create a grid with paint_graph
paint_graph.make_grid_color([[0, 0, 0, 1], [0, 1, 0, 2], [0, 1, 1, 2]])
# Print original graph
paint_graph.print_paint_graph()
# Perform DFS on paint_graph
paint_graph.dfs(1, 2, 4)
#  Print new paint-filled graph
paint_graph.print_paint_graph()

