import random
import chess
from random_player import Random_player
from minimax import Minimax_player

PLAYER_ONE = 0
PLAYER_TWO = 1
WHITE_PLAYER = 0


chess_board = chess.Board()

pieces = chess_board.piece_map()
piece1 = pieces[0]
detailed_piece = piece1.piece_type
color = piece1.color
wah = piece1.symbol()

def determine_white():
    WHITE_PLAYER = random.randint(0,1)
    if WHITE_PLAYER == PLAYER_ONE:
        random_p = Random_player(chess.WHITE, chess_board)
        minimax_p = Random_player(chess.BLACK, chess_board)
    else:
        random_p = Random_player(chess.BLACK, chess_board)
        minimax_p = Random_player(chess.WHITE, chess_board)
    return random_p, minimax_p

player_1, player_2 = determine_white()

def one_move():
    if WHITE_PLAYER == PLAYER_ONE:
        player_2.move()
        player_1.move()
    else:
        player_2.move()
        player_1.move()
    print(chess_board)
    

while not chess_board.is_game_over():
    one_move()


