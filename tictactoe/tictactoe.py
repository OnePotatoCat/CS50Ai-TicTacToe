"""
Tic Tac Toe Player
"""
import copy
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
    x_count = sum(x.count(X) for x in board)
    o_count = sum(o.count(O) for o in board)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    i = 0
    j = 0
    available_actions = [()]

    for row in board:
        for cell in row:
            if cell == EMPTY:
                available_actions.append(i, j)
            j += 1
        i += 1
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = "X"
    else:
        raise Exception("The space is occupied")

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or\
       (board[0][0] == X and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or\
       (board[0][0] == X and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or\
       (board[0][0] == X and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or\
       (board[0][0] == X and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or\
       (board[0][0] == X and board[0][2] == board[1][2] and board[1][2] == board[2][2]) or\
       (board[0][0] == X and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or\
       (board[0][0] == X and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return X
    if (board[0][0] == O and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or\
       (board[0][0] == O and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or\
       (board[0][0] == O and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or\
       (board[0][0] == O and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or\
       (board[0][0] == O and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or\
       (board[0][0] == O and board[0][2] == board[1][2] and board[1][2] == board[2][2]) or\
       (board[0][0] == O and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or\
       (board[0][0] == O and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        return True

    if len(actions(board)) == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1

    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        target = 1
    elif player(board) == O:
        target = -1
    if terminal(board):
        return None

    available_moves = actions(board)
    for move in available_moves:
        if player(board):
            if utility(result(board, move)) == target:
                return

