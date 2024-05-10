"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
        # Initialize counters for X and O
    count_X = 0
    count_O = 0
    
    # Iterate over each row and each cell in the row
    for row in board:
        for cell in row:
            if cell == 'X':
                count_X += 1
            elif cell == 'O':
                count_O += 1
    
    # Compare counts and return the appropriate symbol
    if count_X > count_O:
        return '0'
    else:
        return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_positions = []
    # Iterate through each row with its index
    for i, row in enumerate(board):
        # Iterate through each cell in the row with its index
        for j, value in enumerate(row):
            if value == "EMPTY":
                # If the cell is "EMPTY", append the (i, j) tuple to the result list
                empty_positions.append((i, j))
    return empty_positions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
