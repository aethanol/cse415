'''Default.py
A baroque chess player implemented by Ethan Anderson and Bartholomew Olson
'''
#  7  0  1   UL U UR    -9  -8  -7
#  6     2   L     R    -1      +1
#  5  4  3   DL D DR    +7  +8  +9

import BC_state_etc as BC
import time
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
def find_adjacent_enemy(new_state, move):
    enemy_list = ['p', 'c', 'k', 'f', 'l', 'i', 'w']
    friendly_list = ['P', 'C', 'K', 'F', 'L', 'I', 'W']
    adjacent_enemy = []
    enemy_class = []
    enemy_direction = []
    #Up
    if new_state[move[1]-8] in enemy_list:
        adjacent_enemy.append(move[1]-8)
        enemy_class.append(new_state[move[1]-8])
        enemy_direction.append('U')
    #Up-Right
    elif new_state[move[1]-7] in enemy_list:
        adjacent_enemy.append(move[1]-7)
        enemy_class.append(new_state[move[1]-7])
        enemy_direction.append('UR')
    #Right
    elif new_state[move[1]+1] in enemy_list:
        adjacent_enemy.append(move[1]+1)
        enemy_class.append(new_state[move[1]+1])
        enemy_direction.append('R')
    #Down-Right
    elif new_state[move[1]+9] in enemy_list:
        adjacent_enemy.append(move[1]+9)
        enemy_class.append(new_state[move[1]+9])
        enemy_direction.append('DR')
    #Down
    elif new_state[move[1]+8] in enemy_list:
        adjacent_enemy.append(move[1]+8)
        enemy_class.append(new_state[move[1]+8])
        enemy_direction.append('D')
    #Down-Left
    elif new_state[move[1]+7] in enemy_list:
        adjacent_enemy.append(move[1]+7)
        enemy_class.append(new_state[move[1]+7])
        enemy_direction.append('DL')
    #Left
    elif new_state[move[1]-1] in enemy_list:
        adjacent_enemy.append(move[1]-1)
        enemy_class.append(new_state[move[1]-1])
        enemy_direction.append('L')
    #Up-Left
    elif new_state[move[1]-9] in enemy_list:
        adjacent_enemy.append(move[1]-9)
        enemy_class.append(new_state[move[1]-9])
        enemy_direction.append('UL')

    local_info = [adjacent_enemy, enemy_class, enemy_direction]

    return(local_info)

def move_captures(new_state, previous_state, move, warrior_class):
    local_info = find_adjacent_enemy(new_state, move)
    adjacent_enemy = local_info[0]
    enemy_class = local_info[1]
    enemy_direction = local_info[2]

    if warrior_class == 'p':
        if adjacent_enemy:
            for idx in range(len(adjacent_enemy)):
                


def rank_move(active_piece, previous_state, new_state):
    #rank from -10 to 10 any state for an active piece and it's move

    #-10 is a king capture
    #-5 is a minor piece capture
    #0 does nothing as far as we can see
    #5 is a minor piece capture
    #10 is a king capture

    #Pincher
    #if we can move next to a piece that has a pincher on the opposite side, this ranks 5+

    #Withdrawer
    #if an enemy piece is directly adjacent at the start of the move, this ranks 5+

    #Leaper
    #if an enemy piece is directly adjacent at the start of the move, this ranks 5+

    #Coordinator
    #if the friendly king makes a square whose corners cover an enemy piece, this ranks 5+

    #Freezer
    #if an enemy is directly adjacent at the start of the turn, this ranks 0-2
    #if a higher value enemy is within reach, and won't get the freezer eaten, this ranks 3-5

    #Imitator
    #Depends on the adjacent piece's abilities, i.e. withdrawer or leaper, w/e

    #King
    #if an enemy is directly adjacent, this ranks 5+
    #unless it'll get the king killed

def make_new_board_state(move, previous_state):
    #Move the piece using previous_state and move
    #DOES NOT HANDLE CAPTURES YET
    previous_state[move[1]] = previous_state[move[0]]
    new_state = previous_state
    return(new_state)

#Finds and returns any blockers due to the edge of the board
def find_wall_blockers(piece_location):
#  7  0  1   UL U UR    -9  -8  -7
#  6     2   L     R    -1      +1
#  5  4  3   DL D DR    +7  +8  +9
    blockers = {'up_blocker' : 0
                'up_right_blocker' : 0
                'right_blocker' : 0
                'down_right_blocker' : 0
                'down_blocker' : 0
                'down_left_blocker' : 0
                'left_blocker' : 0
                'up_left_blocker' : 0
                }

    #check for piece on top border
    if piece_location >= 0 and piece_location <= 7:
        blockers[0] = 1
    #check for piece on bottom border
    elif piece_location >= 56 and piece_location <= 63:
        blockers[4] = 1
    #check for piece on left border
    for index in range(0, 7):
        if piece_location == 8 * index:
            blockers[6] = 1
    #check for piece on right border
    for index in range(0, 7):
        if piece_location == ((8 * index) + 7):
            blockers[2] = 1
    #check for piece in any corner
    if piece_location == 0:
        blockers[7] = 1
    elif piece_location == 7:
        blockers[1] = 1
    elif piece_location == 56:
        blockers[5] = 1
    elif piece_location == 63:
        blockers[3] = 1
    return blockers

#Finds and returns a list of legal moves
def find_moves(current_state, piece_location, warrior_class, blockers):
    wall_list = [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8]
    #Find moves for Pincer
    if warrior_class == 'p':
        for idx in range(7):
            #check for moves up
            if blockers[0] == 0:
                up_move = piece_location - idx * 8
                if current_state[up_move] == 0:
                    legal_moves.append([fullbaord_idx, up_move])
                    if up_move in wall_list:
                        blockers[0] = 1
                else:
                     blockers[0] = 1
            #check for moves to the right
            if blockers[2] == 0:
                right_move = piece_location + idx
                if current_state[right_move] == 0:
                    legal_moves.append([piece_location, right_move])
                    if right_move in wall_list:
                        blockers[2] = 1
                else:
                    blockers[2] = 1
            #check for moves down
            if blockers[4] == 0
            down_move = piece_location + idx * 8
                if current_state[down_move] == 0:
                    legal_moves.append([piece_location, down_move])
                    if down_move in wall_list:
                        blockers[4] = 1
                else:
                    blockers[4] = 1
            #check for moves to the left
            if blockers[6] == 0:
                left_move = piece_location - idx
                if current_state[left_move] == 0:
                    legal_moves.append([piece_location, left_move])
                    if left_move in wall_list:
                        blockers[6] = 1
                else:
                     blockers[6] = 1
    #Find moves for King TODO This doesn't consider optional captures for the king
    elif warrior_class == 'k':
        #Up
        if blockers[0] == 0:
            if current_state[piece_location - 8] == 0:
                legal_moves.append([piece_location, piece_location - 8])
        #Up-Right
        if blockers[1] == 0:
            if current_state[piece_location - 7] == 0:
                legal_moves.append([piece_location, piece_location - 7])
        #Right
        if blockers[2] == 0:
            if current_state[piece_location + 1] == 0:
                legal_moves.append([piece_location, piece_location + 1])
        #Down-Right
        if blockers[3] == 0:
            if current_state[piece_location + 9] == 0:
                legal_moves.append([piece_location, piece_location + 9])
        #Down
        if blockers[4] == 0:
            if current_state[piece_location + 8] == 0:
                legal_moves.append([piece_location, piece_location + 8])
        #Down-Left
        if blockers[5] == 0:
            if current_state[piece_location + 7] == 0:
                legal_moves.append([piece_location, piece_location + 7])
        #Left
        if blockers[6] == 0:
            if current_state[piece_location - 1] == 0:
                legal_moves.append([piece_location, piece_location - 1])
        #Up-Left
        if blockers[7] == 0:
            if current_state[piece_location - 9] == 0:
                legal_moves.append([piece_location, piece_location - 9])
    #Find moves for any other piece
    else:
        for idx in range(7):
            #Up
            if blockers[0] == 0:
                up_move = piece_location - idx * 8
                if current_state[up_move] == 0:
                    legal_moves.append([fullbaord_idx, up_move])
                    if up_move in wall_list:
                        blockers[0] = 1
                else:
                     blockers[0] = 1
            #Up-Right
            if blockers[1] == 0:
                up_right_move = piece_location - idx * 7
                if current_state[up_right_move] == 0:
                    legal_moves.append([fullbaord_idx, up_right_move])
                    if up_right_move in wall_list:
                        blockers[1] = 1
                else:
                     blockers[1] = 1
            #Right
            if blockers[2] == 0:
                right_move = piece_location + idx
                if current_state[right_move] == 0:
                    legal_moves.append([piece_location, right_move])
                    if right_move in wall_list:
                        blockers[2] = 1
                else:
                    blockers[2] = 1
            #Down-Right
            if blockers[3] == 0:
                down_right_move = piece_location + idx * 9
                if current_state[down_right_move] == 0:
                    legal_moves.append([piece_location, down_right_move])
                    if down_right_move in wall_list:
                        blockers[3] = 1
                else:
                    blockers[3] = 1
            #Down
            if blockers[4] == 0:
                down_move = piece_location + idx * 8
                if current_state[down_move] == 0:
                    legal_moves.append([piece_location, down_move])
                    if down_move in wall_list:
                        blockers[4] = 1
                else:
                    blockers[4] = 1
            #Down-Left
            if blockers[5] == 0:
                down_left_move = piece_location + idx * 7
                if current_state[down_left_move] == 0:
                    legal_moves.append9[piece_location, down_left_move])
                    if down_left_move in wall_list:
                        blockers[5] = 1
                else:
                     blockers[5] = 1
            #Left
            if blockers[6] == 0:
                left_move = piece_location - idx
                if current_state[left_move] == 0:
                    legal_moves.append9[piece_location, left_move])
                    if left_move in wall_list:
                        blockers[6] = 1
                else:
                     blockers[6] = 1
            #Up-Left
            if blockers[7] == 0:
                up_left_move = piece_location - idx * 9
                if current_state[up_left_move] == 0:
                    legal_moves.append([piece_location, up_left_move])
                    if up_left_move in wall_list:
                        blockers[7] = 1
                else:
                     blockers[7] = 1

    return legal_moves

    #Assumes my pieces are upper case
def checkForMyPiece(slot):
        if slot != 0:
            piece = 1
        elif slot == 0:
            piece = 0
        if slot == 'P' or slot == 'C' or slot == 'L' slot == 'I' or slot == 'W' or slot == 'K' or slot == 'F':
            myPiece = 1
        else:
            myPiece = 0
        warrior_class = slot
        return [piece, myPiece, warrior_class]

    #Assumes their pieces are lower case
def checkForTheirPiece(slot):
        if slot != 0:
            piece = 1
        elif slot == 0:
            piece = 0
        if slot == 'p' or slot == 'c' or slot == 'l' slot == 'i' or slot == 'w' or slot == 'k' or slot == 'f':
            theirPiece = 1
        else:
            theirPiece = 0
        warrior_class = slot
        return [piece, myPiece, warrior_class]



def nickname():
    return "Newman"

def introduce():
    return "I'm Newman Barry, a newbie Baroque Chess agent."

def prepare(player2Nickname):
    pass

def parse(bs): # bs is board string
  '''Translate a board string into the list of lists representation.'''
  b = [[0,0,0,0,0,0,0,0] for r in range(8)]
  rs9 = bs.split("\n")
  rs8 = rs9[1:] # eliminate the empty first item.
  for iy in range(8):
    rss = rs8[iy].split(' ');
    for jx in range(8):
      b[iy][jx] = INIT_TO_CODE[rss[jx]]
  return b
