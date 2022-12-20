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
    from collections import Counter
    from itertools import chain
    counts = Counter(chain.from_iterable(board))
    if counts['X'] == counts['O']:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    list = []
    for index1, value1 in enumerate(board):
        for index2, value2 in enumerate(value1):
            if value2 == EMPTY:
                print(value2)
                print(index2)
                list.append((index1, index2))
    return list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    This is called
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    This is called
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    This is called
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    Not Called
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    This is called
    """
    raise NotImplementedError
