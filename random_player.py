import chess
import random

class Random_player:

    def __init__(self, color, board):
        self.board = board
        self.color = color
        if color == chess.WHITE:
            self.move()
        
    def move(self):
        # get legal moves
        legal_moves = self.board.legal_moves
        list_moves = []
        for move in legal_moves:
            list_moves.append(move)
        
        random_choice = random.randint(0, len(list_moves) - 1)
        self.board.push(list_moves[random_choice])

