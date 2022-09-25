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
    available_actions = set()
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                available_actions.add((i, j))
            j += 1
        i += 1
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] == EMPTY:
        new_board[action[0]][action[1]] = player(board)
    else:
        raise Exception("The space is occupied")

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if (board[0][0] == X and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or\
       (board[1][0] == X and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or\
       (board[2][0] == X and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or\
       (board[0][0] == X and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or\
       (board[0][1] == X and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or\
       (board[0][2] == X and board[0][2] == board[1][2] and board[1][2] == board[2][2]) or\
       (board[0][0] == X and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or\
       (board[2][0] == X and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return X
    if (board[0][0] == O and board[0][0] == board[0][1] and board[0][1] == board[0][2]) or\
       (board[1][0] == O and board[1][0] == board[1][1] and board[1][1] == board[1][2]) or\
       (board[2][0] == O and board[2][0] == board[2][1] and board[2][1] == board[2][2]) or\
       (board[0][0] == O and board[0][0] == board[1][0] and board[1][0] == board[2][0]) or\
       (board[0][1] == O and board[0][1] == board[1][1] and board[1][1] == board[2][1]) or\
       (board[0][2] == O and board[0][2] == board[1][2] and board[1][2] == board[2][2]) or\
       (board[0][0] == O and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or\
       (board[2][0] == O and board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
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
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X is the maximizer
    O is the minimizer
    """
    if terminal(board):
        return None

    moves = []
    if player(board) == X:
        for action in actions(board):
            value = minimizer(result(board, action))

            """
            If value of the move is 1 (certain to be winning move) 
            skip checking remaining moves
            """
            if value == 1:
                return action
            moves.append([value, action])
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        for action in actions(board):
            value = maximizer(result(board, action))

            """
            If value of the move is -1 (certain to be winning move) 
            skip checking remaining moves
            """
            if value == -1:
                return action
            moves.append([value, action])
        return sorted(moves, key=lambda x: x[0])[0][1]


def maximizer(board):
    if terminal(board):
        return utility(board)

    value = -math.inf
    for action in actions(board):
        value = max(value, minimizer(result(board, action)))
    return value


def minimizer(board):
    if terminal(board):
        return utility(board)

    value = math.inf
    for action in actions(board):
        value = min(value, maximizer(result(board, action)))
    return value
