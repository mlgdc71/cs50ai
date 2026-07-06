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
    i, j = action
    if player(board) == X:
        board[i][j] = X
    else:
        board[i][j] = O
    return board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # row + column
    diagonals = []
    anti = []
    for i in range(3):
        coord = board[i][i]
        anticoord = board[i][2 - i]
        diagonals.append(coord)
        anti.append(anticoord)

    total = board + list(zip(*board)) + anti + diagonals

    for i in total:
        if all(instance == X for instance in i):
            return X
        elif all(instance == O for instance in i):
            return O
        else:
            return None

    # diagonal + antidiagonal
    # wait what if we somehow turn the diagonal into a row and put it in the above

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # class action():
    #     def __init__(self, value):
    #         self.value = value

    if player(board) == O:
        if terminal(board):
            return utility(board)
        v = math.inf
        # for action in actions(board):
        #     if min(v, max(utility(result(board, action))) == -1:
        #         return action
        for action in actions(board):
            if utility(result(board, action)) < v:
                v = utility(result(board, action))
                best_action = action

            return best_action
    else:
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            if max(v, min(utility(result(board, action))) == 1:
                return action



