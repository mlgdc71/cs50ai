"""
Tic Tac Toe Player
"""

import math

from pygame import colordict

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
    xcount = sum(instance.count(X) for instance in board)
    if xcount % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # actions = []
    # while actions != []:
    #     for i, j in board[i][j]:
    #         if j == EMPTY:
    #             actions.append((i,j))
    #         else:
    #             return actions
    # return None

    actions = set()
    for i, row in enumerate(board):
        for j, column in enumerate(row):  # refer to diagram
            if row[j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check row, column, one diagonal, one antidiagonal



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
