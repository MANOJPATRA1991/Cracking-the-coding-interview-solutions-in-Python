# How many possible paths are there for a robot to go from point (0,0) to point (X,Y)
# in an X by Y grid, given that a robot can move only in two directions: right and down

# FOLLOW UP
# Design an algorithm to find a path for the robot to move from top left to bottom right
# when some of the spots are off-limit

import functools
import math


def memoize(f):
    """ Minimalistic memoization decorator (*args / **kwargs)
    Based on: http://code.activestate.com/recipes/577219/ """

    cache = {}

    @functools.wraps(f)
    def memf(*args, **kwargs):
        fkwargs = frozenset(kwargs.items())
        if (args, fkwargs) not in cache:
            cache[args, fkwargs] = f(*args, **kwargs)
        return cache[args, fkwargs]
    return memf


class Grid(object):
    """
    Define a point
    Attributes:
        x(Integer): The x-coordinate
        y(Integer): The y-coordinate
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.off_limit_coords = set()

    def mark_off_limit(self, row, col):
        """
        Mark a point as off limit
        Args:
             row: Row number
             col: Column number
        """
        self.off_limit_coords.add((row, col))

    def is_valid(self, row, col):
        """
        Check if point is valid
        Args:
            row: Row number
            col: Column number
        """
        return (0 <= row < self.x and
                0 <= col < self.y and
                (row, col) not in self.off_limit_coords)

    @property
    def calc_num_of_paths(self):
        """
        Calculate number of available paths from
        (0,0) to (X-1, Y-1)
        """
        end_x = self.x - 1
        end_y = self.y - 1
        return math.factorial(end_x + end_y) // \
               (math.factorial(end_x) * math.factorial(end_y))

    @memoize
    def get_path(self, row=0, col=0):
        """
        Return a path from (row, col) to (self.x - 1, self.y - 1)
        Run time: O((X-1)*(Y-1))
        Args:
            row: Starting row number
            col: Starting column number
        """
        destination = (self.x - 1, self.y - 1)
        current = [(row, col)]

        if (row, col) == destination:
            return current

        neighbors = [(row, col + 1), (row + 1, col)]

        for neighbor in neighbors:
            if self.is_valid(*neighbor):
                path_list = self.get_path(*neighbor)
                if path_list and path_list[-1] == destination:
                    return current + path_list

grid = Grid(3, 3)
path = grid.get_path()
print(path)
print(grid.calc_num_of_paths)

grid = Grid(2, 2)
path = grid.get_path()
print(path)
print(grid.calc_num_of_paths)
