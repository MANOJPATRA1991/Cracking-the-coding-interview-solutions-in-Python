# Write an algorithm to print all ways of arranging eight queens
# on an 8x8 chess board so that none of them share the same row, column or diagonal.

import copy


class ChessBoard(object):
    """
    Creates a new chess board
    Attributes:
        queens(dict): A dictionary of rows and columns occupied by queens
        size(int): The size of the board
    """
    def __init__(self, n):
        self.queens = dict()
        self.size = n

    def place(self, row, col):
        """
        Places a queen at a specified row and column
        Args:
            row: Row number
            col: Column number
        """
        self.queens[row] = col

    def is_safe(self, row, col):
        """
        Checks if a row and column is safe to be occupied
        Args:
            row: Row number
            col: Column number
        Returns:
            Boolean: Indicates if a row-column pair is safe
        """
        for x, y in self.queens.items():
            # If row already contains a queen
            if x == row:
                return False

            # If column already contains a queen
            if y == col:
                return False

            # If the position is diagonally present with
            # respect to a queen
            if abs(row - x) == abs(col - y):
                return False

        # Safe
        return True

    @classmethod
    def queens_ways(cls, size, board=None, row=0, queens_left=None):
        """
        Find number of ways to arrange the queens
        Args:
            size: Size of the board
            board: ChessBoard instance
            row: Row number
            queens_left: Number of queens left to arrange
        Returns:
            Number of arrangements possible
        """
        if not board:
            board = cls(size)

        if queens_left is None:
            queens_left = board.size

        # All queens safely placed
        if not queens_left:
            return 1

        total = 0
        # Number of columns = board's size(square matrix)
        for col in range(board.size):
            if board.is_safe(row, col):
                board_copy = copy.deepcopy(board)
                board_copy.place(row, col)
                total += cls.queens_ways(size, board_copy, row + 1, queens_left - 1)
        return total

result = ChessBoard.queens_ways(8)
print(result)
