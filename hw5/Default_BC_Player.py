'''Default.py
A baroque chess player implemented by Ethan Anderson and Bartholomew Olson
'''
#  7  0  1   UL U UR    -9  -8  -7
#  6     2   L     R    -1      +1
#  5  4  3   DL D DR    +7  +8  +9

import BC_state_etc as BC
import time
from collections import defaultdict
import itertools
import math

GameTree = defaultdict()
BOARD_DIM = 8

def makeMove(currentState, currentRemark, timelimit):
    # # Compute the new state for a move.
    # # This is a placeholder that just copies the current state.
    # newState = BC.BC_state(currentState.board)
    #
    # # Fix up whose turn it will be.
    # newState.whose_move = 1 - currentState.whose_move
    #
    # # Construct a representation of the move that goes from the
    # # currentState to the newState.
    # # Here is a placeholder in the right format but with made-up
    # # numbers:
    # move = ((6, 4), (3, 4))
    #
    # # Make up a new remark
    # newRemark = "I'll think harder in some future game. Here's my move"
    #
    # return [[move, newState], newRemark]


    root = currentState
    max_depth = 5
    remaining = timelimit
    start_time = time.time()

    for depth in range(1, max_depth):
        # find how much time we have left, but give it a few seconds to finish the
        # computation of the best possible movie and return
        elapsed_time = time.time() - start_time
        remaining -= elapsed_time
        if remaining < timelimit + 2:
            break


# def minimax(state, depth, whose_move):
#     if depth is 0:
#         # TODO check the
#     else:


def idfs(state, depth):
    if depth == 0:
        return
    else:
        pass
    pass


#     p: pincer # moves like a rook (castle)
#     l: leaper # moves noble but also leaps
#     i: imitator # moves noble but also has to move like
#     w: withdrawer # moves noble
#     k: king # moves like king
#     c: coordinator # moves noble
#     f: freezer # moves noble
#     -: empty square on the board

# checks if a move from start to end is a valid move
# start, end = [row, col]
def can_move(state, start, end):
    if start == end:
        return False
    if start[0] not in range(BOARD_DIM) or start[1] not in range(BOARD_DIM):
        return False
    if end[0] not in range(BOARD_DIM) or end[1] not in range(BOARD_DIM):
        return False

    piece_s = to_piece(state, start)
    if piece_s == '-':
        return False
    piece_e = to_piece(state, end)
    if piece_e != '-':
        return False

    # check if the current player owns the piece TODO: decide where can_move is called from (static eval or not)
    # who = BC.who(BC.INIT_TO_CODE[piece])
    # if state.whose_move != who:
    #     return False
    p_lower = piece_s.lower()
    if p_lower == 'p':
        return can_move_pincer(state, start, end)
    elif p_lower == 'l':
        return can_move_leaper(state, start, end)
    elif p_lower == 'i':
        return can_move_imitator(state, start, end)
    elif p_lower == 'k':
        return can_move_king(state, start, end)
    elif p_lower in ('f', 'c', 'w',):
        return can_move_noble(state, start, end)

# returns the init value from a position on the board
# position = [r, c]
def to_piece(state, position):
    return state.board[position[0]][position[1]]


def can_move_pincer(state, start, end):
    y_df = start[0] - end[0]
    x_df = start[1] - end[1]
    # check if it's trying to move diagonally
    if x_df != 0 and y_df != 0:
        return False

    return can_move_orthogonal(state, start, end)

def can_move_leaper(state, start, end):
    y_df = start[0] - end[0]
    x_df = start[1] - end[1]
    # check if the direction it is moving has a piece directly and can be leaped over

    # else move noble

def can_move_imitator(state, start, end):
    pass

def can_move_king(state, start, end):
    x_df = start[0] - end[0]
    y_df = start[1] - end[1]

    # if you are trying to move more than one spot
    if abs(x_df) > 1 or abs(y_df) > 1:
        return False

    # otherwise check if the spot is blank
    if state.board[end[0]][end[1]] != '-':
        return False

    # TODO check if king is moving into check which will be an illegal move
    return True

def can_move_noble(state, start, end):
    x_df = start[0] - end[0]
    y_df = start[1] - end[1]
    if x_df != 0 and y_df != 0:
        return can_move_diagonal(state, start, end)
    else:
        return can_move_orthogonal(state, start, end)


def can_move_diagonal(state, start, end):
    x_dif = start[0] - end[0]
    y_dif = start[1] - end[1]

    for c in range(x_dif):
        if c == 0:
            continue
        for r in range(y_dif):
            if r == 0:
                continue
            if state.board[start[0] + c][start[1] + r] != '-':
                return False
    return True

def can_move_orthogonal(state, start, end):
    y_df = start[0] - end[0]
    x_df = start[1] - end[1]

    # if we are moving vertical
    if x_df == 0:
        for c in range(1, abs(y_df)):
            direction = y_df / abs(y_df)
            # check if the place is blank
            if state.board[start[1] + c * direction] != '-':
                return False
    # if we are moving horizontal
    elif y_df == 0:
        for r in range(1, abs(x_df)):
            direction = x_df / abs(x_df)
            if state.board[start[0] + r * direction] != '-':
                return False

    else:
        return False


# Static eval performs a static evaluation of the given state.
# The value returned is high if the state is good for WHITE
# and low if the state is good for BLACK.
def staticEval(state):
    # BLACK's pieces are even; WHITE's are odd.
    value = 0
    for r, row in enumerate(state.board):
        for c, col in enumerate(row):
            piece_code = BC.INIT_TO_CODE[col]

            # get the adjacent pieces from the current piece
            adj = get_adj_pieces(state, r, c)

            # if white
            if BC.who(piece_code):
                pass
    pass

def get_adj_pieces(state, r, c):
    adj = []
    pos_deltas = [-1,0,1]
    deltas = itertools.product(pos_deltas, pos_deltas)
    for delta in deltas:
        if (delta[0] == 0 and delta[1] == 0):
            continue
        if r + delta[0] >=0 and c + delta[1] >= 0:
            try:
                piece = state.board[r + delta[0]][c + delta[1]]
                adj.append(piece)
            except IndexError:
                pass
    # print(adj)
    return adj

import sys
import time
def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''This function will spawn a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    '''
    import threading
    class PlayerThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = default

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception as e:
                print(sys.exc_info())
                self.result = default

    pt = PlayerThread()
    pt.start()
    started_at = time.time()
    pt.join(timeout_duration)
    ended_at = time.time()
    diff = ended_at - started_at
    print("Time used in makeMove: %0.4f seconds out of " % diff, timeout_duration)
    if pt.isAlive():
       pass
    else:
        # print("Within the time limit -- nice!")
        return pt.result




def nickname():
    return "Newman"

def introduce():
    return "I'm Newman Barry, a newbie Baroque Chess agent."

def prepare(player2Nickname):
    pass






















    # first_state = []
    # second_state = []
    # third_state = []
    # fourth_state = []
    # fifth_state = []
    #
    # first_state_moves = []
    # second_state_moves = []
    # third_state_moves = []
    # fourth_state_moves = []
    # fifth_state_moves = []
    #
    # best_move = []
    #
    # #mark start time
    #
    # #put the board into a 1D array, should be 64 long
    # #I didn't write parse, I think it makes a square
    # first_state = parse(currentState)
    #
    # #'for' through the first_state array, check for my pieces and their legal moves
    # for piece_location in range(len(first_state)):
    #     #Find all wall blockers
    #     blockers = find_wall_blockers(piece_location)
    #     [piece, myPiece, warrior_class] = checkForMyPiece(initialState[idx])
    #     if piece:
    #         if myPiece:
    #             legal_moves = find_moves(first_state, piece_location, warrior_class, blockers)
    #             for idx in range(len(legal_moves)):
    #                 first_state_moves.append(legal_moves[idx])
    # #Check time!
    #
    # #now take each move and turn it into a new board state
    # #Then find all possible moves from there
    # second_state = make_new_board_state(move, first_state)
    # for piece_location in range(len(second_state)):
    #     blockers = find_wall_blockers(piece_location)
    #     [piece, theirPiece, warrior_class] = checkForTheirPiece
    #     if piece:
    #         if theirPiece:
    #             legal_moves = find_moves(second_state, piece_location, warrior_class, blockers)
    #             for idx in range(len(legal_moves)):
    #                 second_state_moves.append(legal_moves[idx])
    # #Check time!
    #
    # #now take each move and turn it into a new board state
    # #Then find all possible moves from there
    # third_state - make_new_board_state(move, second_state)
    # for piece_location in range(len(third_state)):
    #     blockers - find_wall_blockers(piece_location)
    #     [piece, myPiece, warrior_class] = checkForMyPiece
    #     if piece:
    #         if myPiece:
    #             legal_moves = find_moves(third_state, piece_location, warrior_class, blockers)
    #             for idx in range(len(legal_moves)):
    #                 third_state_moves.append(legal_moves[idx])
    #Check time!


#returns a list of lists containing:
#adjacent enemy locations
#enemy class (king, freezer, etc)
#and direction from the friendly piece
#Still need to determine whether we're upper or lower case
# def find_adjacent_enemy(new_state, move):
#     enemy_list = ['p', 'c', 'k', 'f', 'l', 'i', 'w']
#     friendly_list = ['P', 'C', 'K', 'F', 'L', 'I', 'W']
#     adjacent_enemy = []
#     enemy_class = []
#     enemy_direction = []
#     #Up
#     if new_state[move[1]-8] in enemy_list:
#         adjacent_enemy.append(move[1]-8)
#         enemy_class.append(new_state[move[1]-8])
#         enemy_direction.append('U')
#     #Up-Right
#     elif new_state[move[1]-7] in enemy_list:
#         adjacent_enemy.append(move[1]-7)
#         enemy_class.append(new_state[move[1]-7])
#         enemy_direction.append('UR')
#     #Right
#     elif new_state[move[1]+1] in enemy_list:
#         adjacent_enemy.append(move[1]+1)
#         enemy_class.append(new_state[move[1]+1])
#         enemy_direction.append('R')
#     #Down-Right
#     elif new_state[move[1]+9] in enemy_list:
#         adjacent_enemy.append(move[1]+9)
#         enemy_class.append(new_state[move[1]+9])
#         enemy_direction.append('DR')
#     #Down
#     elif new_state[move[1]+8] in enemy_list:
#         adjacent_enemy.append(move[1]+8)
#         enemy_class.append(new_state[move[1]+8])
#         enemy_direction.append('D')
#     #Down-Left
#     elif new_state[move[1]+7] in enemy_list:
#         adjacent_enemy.append(move[1]+7)
#         enemy_class.append(new_state[move[1]+7])
#         enemy_direction.append('DL')
#     #Left
#     elif new_state[move[1]-1] in enemy_list:
#         adjacent_enemy.append(move[1]-1)
#         enemy_class.append(new_state[move[1]-1])
#         enemy_direction.append('L')
#     #Up-Left
#     elif new_state[move[1]-9] in enemy_list:
#         adjacent_enemy.append(move[1]-9)
#         enemy_class.append(new_state[move[1]-9])
#         enemy_direction.append('UL')
#
#     local_info = [adjacent_enemy, enemy_class, enemy_direction]
#
#     return(local_info)
#
# #Checks to see if a move will capture
# #looks for adjacent enemies in the new state
# #returns:
# #move captures, 1/0 whether it captured or not, for use later on move ranking
# #captured piece location, location of captured piece in the board to clear
# #captured piece class, so we can comment or win the game by capturing a king
# def move_captures(new_state, previous_state, move, warrior_class):
#     enemy_list = ['p', 'c', 'k', 'f', 'l', 'i', 'w']
#     friendly_list = ['P', 'C', 'K', 'F', 'L', 'I', 'W']
#     new_local_info = find_adjacent_enemy(new_state, move)
#     old_local_info = find_adjacent_enemy(previous_state, move)
#     new_adjacent_enemy = new_local_info[0]
#     old_adjacent_enemy = old_local_info[0]
#     new_enemy_class = new_local_info[1]
#     old_enemy_class = old_local_info[1]
#     new_enemy_direction = new_local_info[2]
#     old_enemy_direction = old_local_info[2]
#     captured_piece = []
#     captured_piece_class = []
#
#     if move[1] - move[0] == -8:
#         move_direction = 'U'
#     elif move[1] - move[0] == -7:
#         move_direction = 'UR'
#     elif move[1] - move[0] == 1:
#         move_direction = 'R'
#     elif move[1] - move[0] == 9:
#         move_direction = 'DR'
#     elif move[1] - move[0] == 8:
#         move_direction = 'D'
#     elif move[1] - move[0] == 7:
#         move_direction = 'DL'
#     elif move[1] - move[0] == -1:
#         move_direction = 'L'
#     elif move[1] - move[0] == -9:
#         move_direction = 'UL'
#
#     #Captures for Pincher
#     if warrior_class == 'p':
#         if new_adjacent_enemy:
#             for idx in range(len(new_adjacent_enemy)):
#                 if new_enemy_direction[idx] == 'U':
#                     if new_state[move[1]-16] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]-8)
#                         captured_piece_class.append(new_state[move[1]-8])
#                 elif new_enemy_direction[idx] == 'UR'
#                     if new_state[move[1]-14] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]-7)
#                         captured_piece_class.append(new_state[move[1]-7])
#                 elif new_enemy_direction[idx] == 'R'
#                     if new_state[move[1]+2] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]+1)
#                         captured_piece_class.append(new_state[move[1]+1])
#                 elif new_enemy_direction[idx] == 'DR'
#                     if new_state[move[1]+18] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]+9)
#                         captured_piece_class.append(new_state[move[1]+9])
#                 elif new_enemy_direction[idx] == 'D'
#                     if new_state[move[1]+16] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]+8)
#                         captured_piece_class.append(new_state[move[1]+8])
#                 elif new_enemy_direction[idx] == 'DL'
#                     if new_state[move[1]+14] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]+7)
#                         captured_piece_class.append(new_state[move[1]+7)
#                 elif new_enemy_direction[idx] == 'L'
#                     if new_state[move[1]-2] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]-1)
#                         captured_piece_class.append(new_state[move[1]-1])
#                 elif new_enemy_direction[idx] == 'UL'
#                     if new_state[move[1]-18] == 'p':
#                         move_captures = 1
#                         captured_piece.append(move[1]-9)
#                         captured_piece_class.append(new_state[move[1]-9])
#
#         #Captures for Leaper TODO this is fucked up, leaper can't capture in any direction from where it lands, it has to be in the path already
#         if warrior_class == 'l':
#             for idx in range(len(new_adjacent_enemy)):
#                 if new_enemy_direction[idx] == 'U':
#                     if new_adjacent_enemy[idx]-16 == ' ':
#                         move_captures = 1
#                         new_move[0] = move[0]
#                         new_move[1] =
#                 if new_enemy_direction[idx] == 'UR':
#                     if new_adjacent_enemy[idx]-14 == ' ':
#                 if new_enemy_direction[idx] == 'R':
#                     if new_adjacent_enemy[idx]+2 ' ':
#                 if new_enemy_direction[idx] == 'DR':
#                     if new_adjacent_enemy[idx]+18 ' ':
#                 if new_enemy_direction[idx] == 'D':
#                     if new_adjacent_enemy[idx]+16 ' ':
#                 if new_enemy_direction[idx] == 'DL':
#                     if new_adjacent_enemy[idx]+14 == ' ':
#                 if new_enemy_direction[idx] == 'L':
#                     if new_adjacent_enemy[idx]-2 == ' ':
#                 if new_enemy_direction[idx] == 'UL':
#                     if new_adjacent_enemy[idx] == ' ':
#
#
#
#
#         #Captures for King
#         if warrior_class == 'k':
#             if move_direction in old_enemy_direction:
#                 move_captures = 1
#                 captured_piece.append(move[1])
#                 captured_piece_class.append(previous_state[move[1]])
#
#         #Captures for Withdrawer
#         if warrior_class == 'w':
#             #Checks for adjacent enemy in previous state, if found, and move is oppposite, it captures
#             if move_direction == 'U' and 'D' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]+8)
#                 captured_piece_class.append(previous_state[move[0]+8])
#             elif move_direction == 'UR' and 'DL' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]+7)
#                 captured_piece_class.append(previous_state[move[0]+7])
#             elif move_direction == 'R' and 'L' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]-1)
#                 captured_piece_class.append(previous_state[move[0]-1])
#             elif move_direction == 'DR' and 'UL' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]-9)
#                 captured_piece_class.append(previous_state[move[0]-9])
#             elif move_direction == 'D' and 'U' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]-8)
#                 captured_piece_class.append(previous_state[move[0]-8])
#             elif move_direction == 'DL' and 'UR' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]-7)
#                 captured_piece_class.append(previous_state[move[0]-7])
#             elif move_direction == 'L' and 'R' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]+1)
#                 captured_piece_class.append(previous_state[move[0]+1])
#             elif move_direction == 'UL' and 'DR' in old_adjacent_enemy:
#                 move_captures = 1
#                 captured_piece.append(move[0]+9)
#                 captured_piece_class.append(previous_state[move[0]+9])
#
#         #Captures for the Coordinator
#         if warrior_class == 'c':
#             coordinator_x = move[1] % 8
#             coordinator_y = move[1] / 8
#             for idx in len(previous_state):
#                 if previous_state[idx] == 'k':
#                     king_location = idx
#             king_x = king_location % 8
#             king_y = king_location / 8
#
#             a_corner = coordinator_y * 8 + king_x
#             b_corner = king_y * 8 + coordinator_x
#
#             if previous_state[a_corner] in enemy_list:
#                 move_captures = 1
#                 captured_piece.append(a_corner)
#                 captured_piece_class.append(previous_state[a_corner])
#             if previous_state[b_corner] in enemy_list:
#                 move_captures = 1
#                 captured_piece.append(b_corner)
#                 captured_piece_class.append(previous_state[b_corner])
#
#         #Captures for the leaper
#         #Still need to fix the legal moves for Leaper and add moves that jump a piece
#
#         #Captures for the Imitator
#         if warrior_class == 'i':
#             if 'w' in old_adjacent_enemy:
#                 for idx in range(len(old_adjacent_enemy)):
#                     if old_adjacent_enemy[idx] == 'w':
#                         withdrawer_grid_number = idx
#                 withdrawer_location = old_enemy_direction[withdrawer_grid_number]
#                 if move_direction == opposite(withdrawer_location):
#                     move_captures = 1
#                     captured_piece.append(old_adjacent_enemy[withdrawer_grid_number])
#                     captured_piece_class.append(previous_state[old_adjacent_enemy[withdrawer_grid_number]])
#             if 'p' in new_adjacent_enemy:
#                 for idx in range(len(new_adjacent_enemy)):
#                     if new_enemy_direction[idx] == 'U':
#                         if new_state[move[1]-16] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]-8)
#                             captured_piece_class.append(new_state[move[1]-8])
#                     elif new_enemy_direction[idx] == 'UR'
#                         if new_state[move[1]-14] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]-7)
#                             captured_piece_class.append(new_state[move[1]-7])
#                     elif new_enemy_direction[idx] == 'R'
#                         if new_state[move[1]+2] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]+1)
#                             captured_piece_class.append(new_state[move[1]+1])
#                     elif new_enemy_direction[idx] == 'DR'
#                         if new_state[move[1]+18] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]+9)
#                             captured_piece_class.append(new_state[move[1]+9])
#                     elif new_enemy_direction[idx] == 'D'
#                         if new_state[move[1]+16] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]+8)
#                             captured_piece_class.append(new_state[move[1]+8])
#                     elif new_enemy_direction[idx] == 'DL'
#                         if new_state[move[1]+14] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]+7)
#                             captured_piece_class.append(new_state[move[1]+7)
#                     elif new_enemy_direction[idx] == 'L'
#                         if new_state[move[1]-2] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]-1)
#                             captured_piece_class.append(new_state[move[1]-1])
#                     elif new_enemy_direction[idx] == 'UL'
#                         if new_state[move[1]-18] == 'p':
#                             move_captures = 1
#                             captured_piece.append(move[1]-9)
#                             captured_piece_class.append(new_state[move[1]-9])
#
#             if 'c' in new_adjacent_enemy:
#                 coordinator_x = move[1] % 8
#                 coordinator_y = move[1] / 8
#                 for idx in len(previous_state):
#                     if previous_state[idx] == 'k':
#                         king_location = idx
#                 king_x = king_location % 8
#                 king_y = king_location / 8
#
#                 a_corner = coordinator_y * 8 + king_x
#                 b_corner = king_y * 8 + coordinator_x
#
#                 if previous_state[a_corner] in enemy_list:
#                     move_captures = 1
#                     captured_piece.append(a_corner)
#                     captured_piece_class.append(previous_state[a_corner])
#                 if previous_state[b_corner] in enemy_list:
#                     move_captures = 1
#                     captured_piece.append(b_corner)
#                     captured_piece_class.append(previous_state[b_corner])
#
#             if 'k' in new_adjacent_enemy:
#                 if warrior_class == 'k':
#                         if move_direction in old_adjacent_enemy:
#                             move_captures = 1
#                             captured_piece.append(move[1])
#                             captured_piece_class.append(previous_state[move[1]])
#
#
#
#     return(move_captures, captured_piece_location, captured_piece_class, new_move)
#
# def opposite(direction):
#     if direction == 'U':
#         opposite = 'D'
#     elif direction == 'UR':
#         opposite = 'DL'
#     elif direction == 'R':
#         opposite = 'L'
#     elif direction == 'DR':
#         opposite = 'UL'
#     elif direction == 'D':
#         opposite = 'U'
#     elif direction == 'DL':
#         opposite = 'UR'
#     elif direction == 'L':
#         opposite = 'R'
#     elif direction == 'UL':
#         opposite = 'DR'
#     return opposite
#
# def rank_move(active_piece, previous_state, new_state):
#     #rank from -10 to 10 any state for an active piece and it's move
#
#     #-10 is a king capture
#     #-5 is a minor piece capture
#     #0 does nothing as far as we can see
#     #5 is a minor piece capture
#     #10 is a king capture
#
#     #Pincher
#     #if we can move next to a piece that has a pincher on the opposite side, this ranks 5+
#
#     #Withdrawer
#     #if an enemy piece is directly adjacent at the start of the move, this ranks 5+
#
#     #Leaper
#     #if an enemy piece is directly adjacent at the start of the move, this ranks 5+
#
#     #Coordinator
#     #if the friendly king makes a square whose corners cover an enemy piece, this ranks 5+
#
#     #Freezer
#     #if an enemy is directly adjacent at the start of the turn, this ranks 0-2
#     #if a higher value enemy is within reach, and won't get the freezer eaten, this ranks 3-5
#
#     #Imitator
#     #Depends on the adjacent piece's abilities, i.e. withdrawer or leaper, w/e
#
#     #King
#     #if an enemy is directly adjacent, this ranks 5+
#     #unless it'll get the king killed
#
# def make_new_board_state(move, previous_state):
#     #Move the piece using previous_state and move
#     #DOES NOT HANDLE CAPTURES YET
#     previous_state[move[1]] = previous_state[move[0]]
#     new_state = previous_state
#     return(new_state)
#
# #Finds and returns any blockers due to the edge of the board
# def find_wall_blockers(piece_location):
# #  7  0  1   UL U UR    -9  -8  -7
# #  6     2   L     R    -1      +1
# #  5  4  3   DL D DR    +7  +8  +9
#     blockers = {'up_blocker' : 0
#                 'up_right_blocker' : 0
#                 'right_blocker' : 0
#                 'down_right_blocker' : 0
#                 'down_blocker' : 0
#                 'down_left_blocker' : 0
#                 'left_blocker' : 0
#                 'up_left_blocker' : 0
#                 }
#
#     #check for piece on top border
#     if piece_location >= 0 and piece_location <= 7:
#         blockers[0] = 1
#     #check for piece on bottom border
#     elif piece_location >= 56 and piece_location <= 63:
#         blockers[4] = 1
#     #check for piece on left border
#     for index in range(0, 7):
#         if piece_location == 8 * index:
#             blockers[6] = 1
#     #check for piece on right border
#     for index in range(0, 7):
#         if piece_location == ((8 * index) + 7):
#             blockers[2] = 1
#     #check for piece in any corner
#     if piece_location == 0:
#         blockers[7] = 1
#     elif piece_location == 7:
#         blockers[1] = 1
#     elif piece_location == 56:
#         blockers[5] = 1
#     elif piece_location == 63:
#         blockers[3] = 1
#     return blockers
#
# #Finds and returns a list of legal moves TODO Tie each move to it's parent move, so they can be tracked properly
# def find_moves(current_state, piece_location, warrior_class, blockers):
#     wall_list = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8]
#     #Find moves for Pincer
#     if warrior_class == 'p':
#         for idx in range(7):
#             #check for moves up
#             if blockers[0] == 0:
#                 up_move = piece_location - idx * 8
#                 if current_state[up_move] == 0:
#                     legal_moves.append([fullbaord_idx, up_move])
#                     if up_move in wall_list:
#                         blockers[0] = 1
#                 else:
#                      blockers[0] = 1
#             #check for moves to the right
#             if blockers[2] == 0:
#                 right_move = piece_location + idx
#                 if current_state[right_move] == 0:
#                     legal_moves.append([piece_location, right_move])
#                     if right_move in wall_list:
#                         blockers[2] = 1
#                 else:
#                     blockers[2] = 1
#             #check for moves down
#             if blockers[4] == 0
#             down_move = piece_location + idx * 8
#                 if current_state[down_move] == 0:
#                     legal_moves.append([piece_location, down_move])
#                     if down_move in wall_list:
#                         blockers[4] = 1
#                 else:
#                     blockers[4] = 1
#             #check for moves to the left
#             if blockers[6] == 0:
#                 left_move = piece_location - idx
#                 if current_state[left_move] == 0:
#                     legal_moves.append([piece_location, left_move])
#                     if left_move in wall_list:
#                         blockers[6] = 1
#                 else:
#                      blockers[6] = 1
#     #Find moves for King Any move is possible, some will capture, considered in move_captures()
#     elif warrior_class == 'k':
#         #Up
#         if blockers[0] == 0:
#             legal_moves.append([piece_location, piece_location - 8])
#         #Up-Right
#         if blockers[1] == 0:
#             legal_moves.append([piece_location, piece_location - 7])
#         #Right
#         if blockers[2] == 0:
#             legal_moves.append([piece_location, piece_location + 1])
#         #Down-Right
#         if blockers[3] == 0:
#             legal_moves.append([piece_location, piece_location + 9])
#         #Down
#         if blockers[4] == 0:
#             legal_moves.append([piece_location, piece_location + 8])
#         #Down-Left
#         if blockers[5] == 0:
#             legal_moves.append([piece_location, piece_location + 7])
#         #Left
#         if blockers[6] == 0:
#             legal_moves.append([piece_location, piece_location - 1])
#         #Up-Left
#         if blockers[7] == 0:
#             legal_moves.append([piece_location, piece_location - 9])
#     #Find moves for any other piece
#     else:
#         for idx in range(7):
#             #Up
#             if blockers[0] == 0:
#                 up_move = piece_location - idx * 8
#                 if current_state[up_move] == 0:
#                     legal_moves.append([fullbaord_idx, up_move])
#                     if up_move in wall_list:
#                         blockers[0] = 1
#                 else:
#                      blockers[0] = 1
#             #Up-Right
#             if blockers[1] == 0:
#                 up_right_move = piece_location - idx * 7
#                 if current_state[up_right_move] == 0:
#                     legal_moves.append([fullbaord_idx, up_right_move])
#                     if up_right_move in wall_list:
#                         blockers[1] = 1
#                 else:
#                      blockers[1] = 1
#             #Right
#             if blockers[2] == 0:
#                 right_move = piece_location + idx
#                 if current_state[right_move] == 0:
#                     legal_moves.append([piece_location, right_move])
#                     if right_move in wall_list:
#                         blockers[2] = 1
#                 else:
#                     blockers[2] = 1
#             #Down-Right
#             if blockers[3] == 0:
#                 down_right_move = piece_location + idx * 9
#                 if current_state[down_right_move] == 0:
#                     legal_moves.append([piece_location, down_right_move])
#                     if down_right_move in wall_list:
#                         blockers[3] = 1
#                 else:
#                     blockers[3] = 1
#             #Down
#             if blockers[4] == 0:
#                 down_move = piece_location + idx * 8
#                 if current_state[down_move] == 0:
#                     legal_moves.append([piece_location, down_move])
#                     if down_move in wall_list:
#                         blockers[4] = 1
#                 else:
#                     blockers[4] = 1
#             #Down-Left
#             if blockers[5] == 0:
#                 down_left_move = piece_location + idx * 7
#                 if current_state[down_left_move] == 0:
#                     legal_moves.append9[piece_location, down_left_move])
#                     if down_left_move in wall_list:
#                         blockers[5] = 1
#                 else:
#                      blockers[5] = 1
#             #Left
#             if blockers[6] == 0:
#                 left_move = piece_location - idx
#                 if current_state[left_move] == 0:
#                     legal_moves.append9[piece_location, left_move])
#                     if left_move in wall_list:
#                         blockers[6] = 1
#                 else:
#                      blockers[6] = 1
#             #Up-Left
#             if blockers[7] == 0:
#                 up_left_move = piece_location - idx * 9
#                 if current_state[up_left_move] == 0:
#                     legal_moves.append([piece_location, up_left_move])
#                     if up_left_move in wall_list:
#                         blockers[7] = 1
#                 else:
#                      blockers[7] = 1
#
#     return legal_moves
#
#     #Assumes my pieces are upper case
# def checkForMyPiece(slot):
#         if slot != 0:
#             piece = 1
#         elif slot == 0:
#             piece = 0
#         if slot == 'P' or slot == 'C' or slot == 'L' slot == 'I' or slot == 'W' or slot == 'K' or slot == 'F':
#             myPiece = 1
#         else:
#             myPiece = 0
#         warrior_class = slot
#         return [piece, myPiece, warrior_class]
#
#     #Assumes their pieces are lower case
# def checkForTheirPiece(slot):
#         if slot != 0:
#             piece = 1
#         elif slot == 0:
#             piece = 0
#         if slot == 'p' or slot == 'c' or slot == 'l' slot == 'i' or slot == 'w' or slot == 'k' or slot == 'f':
#             theirPiece = 1
#         else:
#             theirPiece = 0
#         warrior_class = slot
#         return [piece, myPiece, warrior_class]

