#!/usr/bin/python3
"""N-queens puzzle solver.

Computes all possible arrangements for N
queens on an NxN chessboard, with no queens threatening each other.

Example:
    $ ./101-nqueens.py N

N should be an integer greater than or equal to 4.

Attributes:
    chess_board (list): A two-dimensional list that represents the chessboard.
    possible_solutions (list): A list containing all solutions.

A solution is represented in the format [[r, c], [r, c], ..., [r, c]]
where `r` and `c` indicate the row and column, respectively, for a queen
to be placed on the chessboard.
"""
import sys


def setup_board(size):
    """Set up an `size`x`size` chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for _ in range(size)]
    [row.append(' ') for _ in range(size) for row in chess_board]
    return chess_board


def deepcopy_board(chess_board):
    """Generate a deepcopy of a chessboard."""
    if isinstance(chess_board, list):
        return list(map(deepcopy_board, chess_board))
    return chess_board


def derive_solution(chess_board):
    """Generate the list representation of a solved chessboard."""
    solution = []
    for row in range(len(chess_board)):
        for column in range(len(chess_board)):
            if chess_board[row][column] == "Q":
                solution.append([row, column])
                break
    return solution


def eliminate_positions(chess_board, row, column):
    """Mark positions on a chessboard that are not safe.

    All positions where queens can't be placed
    safely are marked with 'x'.

    Args:
        chess_board (list): The current chessboard.
        row (int): The row where the latest queen was placed.
        column (int): The column where the latest queen was placed.
    """
    for i in range(len(chess_board)):
        # X out all in same row
        chess_board[row][i] = "x" if i != column else chess_board[row][i]
        # X out all in same column
        chess_board[i][column] = "x" if i != row else chess_board[i][column]
        if row + i < len(chess_board):  # Diagonal positions
            if column + i < len(chess_board):
                chess_board[row + i][column + i] = "x"
            if column - i >= 0:
                chess_board[row + i][column - i] = "x"
        if row - i >= 0:  # Diagonal positions
            if column + i < len(chess_board):
                chess_board[row - i][column + i] = "x"
            if column - i >= 0:
                chess_board[row - i][column - i] = "x"


def solve_puzzle(chess_board, row, queens, possible_solutions):
    """Solve the N-queens puzzle using recursion.

    Args:
        chess_board (list): The current chessboard.
        row (int): The current row.
        queens (int): The number of queens currently placed.
        possible_solutions (list): A list containing all solutions.
    Returns:
        possible_solutions
    """
    if queens == len(chess_board):
        possible_solutions.append(derive_solution(chess_board))
        return possible_solutions

    for column in range(len(chess_board)):
        if chess_board[row][column] == " ":
            tmp_board = deepcopy_board(chess_board)
            tmp_board[row][column] = "Q"
            eliminate_positions(tmp_board, row, column)
            possible_solutions = solve_puzzle(tmp_board, row + 1, queens + 1,
                                              possible_solutions)

    return possible_solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = setup_board(int(sys.argv[1]))
    possible_solutions = solve_puzzle(chess_board, 0, 0, [])
    for solution in possible_solutions:
        print(solution)
